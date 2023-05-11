from constants import ENDPOINT
import requests

class User:
    def __init__(self, username: str, token: str):
        self.token = token
        self.username = username
        self.endpoint = ENDPOINT
        self.headers = {
            "X-USER-TOKEN": self.token,
            "Content-Type": "application/json"
        }

    def create_user(self):
        payload = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        headers = {"Content-Type": "application/json"}

        return requests.request("POST", self.endpoint, json=payload, headers=headers).json()

    def update_user(self, new_token: str):
        payload = {"newToken": new_token}
        response =  requests.request("PUT", self.endpoint + f"{self.username}", json=payload, headers=self.headers).json()
        self.headers["X-USER-TOKEN"] = new_token

        return response

    def delete_user(self):

        return requests.request("DELETE", self.endpoint + f"{self.username}", headers=self.headers).json()

user7 = User("easyname777", "secrettoken")
