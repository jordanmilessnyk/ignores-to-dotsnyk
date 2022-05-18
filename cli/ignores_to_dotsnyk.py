import sys
import click
from ignores import retrieve_ignores, ignores_to_snyk


@click.command()
@click.option('-o', '--org-id', required=True)
@click.option('-p', '--project-id', required=True)
@click.option('-a', '--api-key', required=True)
@click.option('-d', '--directory')
def ignores_to_dotsnyk(org_id, project_id, api_key, directory):

    try:
        issues = retrieve_ignores(org_id, project_id, api_key)
        issues_yaml = ignores_to_snyk(issues)

        write_file = '{}/.snyk'.format(directory) if directory else '.snyk'

        with open(write_file, 'w') as snyk_file:
            snyk_file.write(issues_yaml)

    except Exception as e:
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    ignores_to_dotsnyk()
