import sys
import json

import requests

if __name__ == "__main__":
    username = sys.argv[1]
    request = "https://api.github.com/users/{}/events".format(username)
    response = requests.get(request)
    events = response.json()
    print(events[0]['created_at'])
