import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error occurred during request: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                json_data = json.loads(response_body)
                return json_data
            except json.JSONDecodeError as e:
                print(f"Error occurred during JSON decoding: {e}")
                return None
        else:
            return None
