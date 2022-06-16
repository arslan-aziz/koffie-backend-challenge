from urllib.parse import urljoin, urlencode
import requests

from fastapi.exceptions import HTTPException


class ApiBase:
    def __init__(self, url: str, api_name: str):
        self.url = url
        self.api_name = api_name

    def get_request(self, endpoint: str, params: dict):
        """Make a get request."""
        endpoint = endpoint + "?" + urlencode(params)
        full_url = urljoin(self.url, endpoint)
        response = requests.get(full_url)
        try:
            response.raise_for_status()
        except requests.exceptions.Timeout:
            raise HTTPException(500, f"{self.api_name} timed out.")
        except requests.exceptions.TooManyRedirects:
            raise HTTPException(500, f"{self.api_name} redirected too many times.")
        except requests.exceptions.RequestException:
            raise HTTPException(500, f"{self.api_name} had an unknown error.")

        return response.json()
