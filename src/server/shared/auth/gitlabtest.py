import requests

class GitlabAPIClient:
    def __init__(self, base_url, token):
        self.token = token
        self.base_url = base_url
        self.headers = {"PRIVATE-TOKEN": token, "content-type": "multipart/form-data"}

    def get(self, endpoint: str):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            logging.error("🚨  HTTP Request Error")
            exit(EXIT_CODE)
        return response

gl = GitlabAPIClient(
   "https://gitlab.com/api/v4",
   os.getenv("GITLAB_READONLY_TOKEN"),)
