import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        response = requests.get(self.url)
        
        return response.content

    def load_json(self):
        pass
        json_response = requests.get(self.url).json()
        return json_response
