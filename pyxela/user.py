from constants import PIXELA_ENDPOINT as endpoint
import requests

class User:
    def __init__(self, username:str, token:str):
        self.token = token
        self.username = username
        self.base_endpoint = endpoint

    def create_user(self):
        payload = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        headers = {"Content-Type": "application/json"}
        return requests.request("POST", self.base_endpoint, json=payload, headers=headers).json()

    def update_user(self, new_token:str):
        payload = {"newToken": new_token}
        headers = {
            "X-USER-TOKEN": self.token,
            "Content-Type": "application/json"
        }

        self.token = new_token
        return requests.request("PUT", self.base_endpoint + f"{self.username}" , json=payload, headers=headers).json()

    def delete_user(self):
        headers = {
            "X-USER-TOKEN": self.token,
            "Content-Type": "application/json"
        }

        return requests.request("DELETE", self.base_endpoint + f"{self.username}" , headers=headers).json()

