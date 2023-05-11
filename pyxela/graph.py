import requests
from constants import ENDPOINT
from colors import Colors
from enum import Enum
from user import User, user7

class GraphConfig(Enum):
    _id: str = ""
    name: str = ""
    unit: str = ""
    _type: str = ""
    color: Colors = ""

class Graph:
    def __init__(self, user: User):
        self.token = user.token
        self.endpoint = user.endpoint + user.username + "/graphs"
        self.headers = user.headers

    def create_graph(
            self,
            graph_id: GraphConfig._id,
            graph_name: GraphConfig.name,
            unit: GraphConfig.unit,
            _type: GraphConfig._type,
            color: GraphConfig.color
    ):

        payload = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": _type,
            "color": color
        }

        return requests.request("POST", self.endpoint, json=payload, headers=self.headers).json()

    def update_graph(
            self,
            graph_id: GraphConfig._id,
            graph_name: GraphConfig.name,
            unit: GraphConfig.unit,
            _type: GraphConfig._type,
            color: GraphConfig.color
    ):

        payload = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": _type,
            "color": color
        }

        return requests.request("PUT", self.endpoint + f"/{graph_id}", json=payload, headers=self.headers).json()

    def delete_graph(self, graph_id: str):
        return requests.request("DELETE", self.endpoint + f"/{graph_id}", headers=self.headers).json()

    def get_graph_definitions(self):
        return requests.request("GET", self.endpoint, headers=self.headers).json()

    def get_a_graph_definition(self, graph_id: str):
        return requests.request("GET", self.endpoint + f"/{graph_id}/graph-def", headers=self.headers).json()

graph7 = Graph(user7)
