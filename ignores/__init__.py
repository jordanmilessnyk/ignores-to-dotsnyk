import requests
import yaml


def retrieve_ignores(org_id: str, project_id: str, api_key: str) -> dict:

    request_url = f'https://snyk.io/api/v1/org/{org_id}/project/{project_id}/ignores'
    request_header = {'Authorization': f'token {api_key}'}

    r = requests.get(request_url, headers=request_header)
    response_json = purge_keys(r.json())

    return response_json


def purge_keys(ignores: dict) -> dict:

    issues = ignores.keys()

    for issue in issues:
        ignores_list = ignores[issue]
        for issue_obj in ignores_list:
            [issue_obj['*'].pop(key) for key in ['ignoredBy', 'reasonType', 'disregardIfFixable']]

    return ignores


def ignores_to_snyk(issues_json: dict) -> str:

    full_ignore_json = {
        'version': 'v1.25.0',
        'ignore': issues_json}

    return yaml.dump(full_ignore_json)

