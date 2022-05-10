from io import StringIO

import requests
import yaml


def retrieve_issues(org_id: str, project_id: str, api_key: str) -> dict:

    request_url = f'https://snyk.io/api/v1/org/{org_id}/project/{project_id}/ignores'
    request_header = {'Authorization': f'token {api_key}'}

    r = requests.get(request_url, headers=request_header)

    return r.json()


def issues_to_snyk(issues_json: dict) -> str:

    full_ignore_json = {
        'version': 'v1.25.0',
        'ignore': issues_json}

    return yaml.dump(full_ignore_json)
