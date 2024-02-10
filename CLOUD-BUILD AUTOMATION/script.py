import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

repo_owner=os.getenv("repo_owner")
repo_name=os.getenv("repo_name")
token=os.getenv("token")
workflow_name=os.getenv("workflow_name")


def trigger():

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_name}/dispatches"
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",  # Add any headers you need
        "X-GitHub-Api-Version": "2022-11-28"
    }

    data = {"ref":"main"}


    requests.post(url, headers=headers, json=data)
    print("Your Workflow run has been triggered and is In Progress")

    return None

def get_all_runs():
    url=f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",  # Add any headers you need
        "X-GitHub-Api-Version": "2022-11-28"
    }

    data = {"ref":"main"}

    response=requests.get(url, headers=headers, json=data)

    return response.json().get('workflow_runs', [])[0]['id']

def run_status(run_id=None):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Extract and return the status field
        status = json_data.get('status')
        return status
    else:
        # Print an error message for non-OK responses
        print(f"Error: Unable to fetch run status. Status code: {response.status_code}")
        return None



def get_dockerhub_image_details(repository, tag='latest', username=None, password=None):
    url = f'https://hub.docker.com/v2/repositories/{repository}/tags/{tag}/'

    # Set up authentication if username and password are provided
    auth = None
    if username and password:
        auth = (username, password)

    # Make the request to Docker Hub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Extract and print the artifact URL
        artifact_url = json_data.get('images', [{}])[0].get('digest')
        return artifact_url
    else:
        # Print an error message for non-OK responses
        print(f"Error: Unable to fetch image details. Status code: {response.status_code}")
        return None

def main():
    # Replace these with your Docker Hub repository details
    username=os.getenv("dockerhub_username")
    password=os.getenv("dockerhub_password")
    repository=os.getenv("dockerhub_repository")

    trigger()
    last_run_id=get_all_runs()

    
    status = 'in_progress'
    while status == 'in_progress':
        status = run_status(last_run_id)
        time.sleep(20)
        print("Wrokflow run Completed!")
    # Fetch artifact URL for the latest tag
    artifact_url = get_dockerhub_image_details(repository, username=username, password=password)
    time.sleep(1)
    if artifact_url:
        print(f"Artifact URL for {repository}:")
        print(artifact_url)
        print(f"Your workflow run id is: {last_run_id}")
    else:
        print("Failed to retrieve artifact URL.")

if __name__ == "__main__":
    main()






