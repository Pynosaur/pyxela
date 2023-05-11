import requests
from constants import colors, PIXELA_ENDPOINT as endpoint

class Graph:
    def __init__(self, token, username):
        self.token = token
        self.base_endpoint = endpoint + username + "/graphs"

    def create_graph(self, graph_id:str, graph_name:str, unit:str, _type:str, color:str):
        if colors.get(color, 0) == 0:
            color = colors["black"]
            return "Invalid color, defaulting to black"
        else:
            color = colors.get(color)
        
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

    def update_graph(self, graph_id:str, graph_name:str, unit:str, _type:str, color:str):
        if colors.get(color, 0) == 0:
            color = colors["black"]
            return "Invalid color, defaulting to black"
        else:
            color = colors.get(color)

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


    def delete_graph(self, graph_id:str):

        headers = {"X-USER-TOKEN": self.token}

        return requests.request("DELETE", self.base_endpoint + f"/{graph_id}", headers=headers).json()
    
    def get_graph_definitions(self):
        headers = {"X-USER-TOKEN": self.token}

        return requests.request("GET", self.base_endpoint, headers=headers).json()

    def get_a_graph_definition(self, graph_id:str):
        headers = {"X-USER-TOKEN": self.token}

        return requests.request("GET", self.base_endpoint + f"/{graph_id}/graph-def", headers=headers).json()
