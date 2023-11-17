import os
import requests

def download_file(url, destination):
    response = requests.get(url)
    try:
        response.raise_for_status()
        with open(destination, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {url} to {destination}")
    except requests.RequestException as e:
        print(f"Failed to download {url}. Error: {e}")

def download_all_files_from_github(repo_owner, repo_name, output_directory):
    github_api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
    response = requests.get(github_api_url)

    try:
        response.raise_for_status()
        files = response.json()

        for file_info in files:
            if file_info["type"] == "file":
                file_name = file_info["name"]
                file_url = file_info["download_url"]
                destination_path = os.path.join(output_directory, file_name)
                download_file(file_url, destination_path)

    except requests.RequestException as e:
        print(f"Failed to fetch files from GitHub. Error: {e}")

# GitHub repository details
repo_owner = "MHin1"
repo_name = "MenuFetcher"

# Output directory
output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Downloads")
os.makedirs(output_directory, exist_ok=True)

# Download all files from the GitHub repository
download_all_files_from_github(repo_owner, repo_name, output_directory)

# Prompt user to press Enter at the end
input("Press Enter to continue...")