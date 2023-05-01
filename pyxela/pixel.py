from constants import colors

import requests
from datetime import date
from constants import PIXELA_ENDPOINT, USER_TOKEN

GRAPH_ID = 'test-graph'
PIXEL_DATE = str(date.today())
QUANTITY = '1'

headers = {
    'X-USER-TOKEN': USER_TOKEN,
}

pixel_params = {
    'date': PIXEL_DATE,
    'quantity': QUANTITY,
}

response = requests.post(url=f'{PIXELA_ENDPOINT}/v1/users/a-know/graphs/{GRAPH_ID}', json=pixel_params, headers=headers)
response.raise_for_status()
