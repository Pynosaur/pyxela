import requests
from constants import PIXELA_ENDPOINT
from colors import Colors
from enum import Enum


class GraphConfig(Enum):
    id: str
    name: str
    unit: str
    type: str
    color: Colors


class Graph:
    def __init__(self, token, username):
        self.token = token
        self.base_endpoint = PIXELA_ENDPOINT + username + "/graphs"

    def create_graph(
            self,
            graph_id: GraphConfig.id,
            graph_name: GraphConfig.name,
            unit: GraphConfig.unit,
            _type: GraphConfig.type,
            color: GraphConfig.color
    ):

        payload = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": _type,
            "color": color
        }
        headers = {
            "X-USER-TOKEN": self.token,
            "Content-Type": "application/json"
        }

        return requests.request("POST", self.base_endpoint, json=payload, headers=headers).json()

    def update_graph(
            self,
            graph_id: GraphConfig.id,
            graph_name: GraphConfig.name,
            unit: GraphConfig.unit,
            _type: GraphConfig.type,
            color: GraphConfig.color
    ):

        payload = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": _type,
            "color": color
        }
        headers = {
            "X-USER-TOKEN": self.token,
            "Content-Type": "application/json"
        }

        return requests.request("PUT", self.base_endpoint + f"/{graph_id}", json=payload, headers=headers).json()

    def delete_graph(self, graph_id: str):

        headers = {"X-USER-TOKEN": self.token}

        return requests.request("DELETE", self.base_endpoint + f"/{graph_id}", headers=headers).json()

    def get_graph_definitions(self):
        headers = {"X-USER-TOKEN": self.token}

        return requests.request("GET", self.base_endpoint, headers=headers).json()

    def get_a_graph_definition(self, graph_id: str):
        headers = {"X-USER-TOKEN": self.token}

        return requests.request("GET", self.base_endpoint + f"/{graph_id}/graph-def", headers=headers).json()
