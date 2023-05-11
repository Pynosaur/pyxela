import requests
from graph import Graph, graph7

class Pixel:
    def __init__(self, graph: Graph, graph_id):
        self.endpoint = graph.endpoint + f"/{graph_id}"
        self.token = graph.token
        self.headers = graph.headers

    def create_pixel(self, date:str, quantity:str):
        payload = {
            "date": date,
            "quantity": quantity
        }

        return requests.request("POST", self.endpoint, json=payload, headers=self.headers).json()

    def get_pixel(self, date:str):

        return requests.request("GET", self.endpoint + f"/{date}", headers=self.headers).json()

    def update_pixel(self, date:str, quantity:str):

        payload = {
            "quantity": quantity
        }

        return requests.request("PUT", self.endpoint + f"/{date}", json=payload, headers=self.headers).json()

    def delete_pixel(self, date:str):

        return requests.request("DELETE", self.endpoint + f"/{date}", headers=self.headers).json()
