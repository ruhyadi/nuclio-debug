
from pprintpp import pprint
import requests
import json

dicts = {
    'per_page': 1,
    'page': 8
}

response = requests.get(
    url='https://api.github.com/repos/nuclio/nuclio/releases/tags/1.5.16'
)

pprint(response.json())