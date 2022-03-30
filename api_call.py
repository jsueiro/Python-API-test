import requests
import json


try:
    response = requests.get(
        'http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()

    res = json.dumps(response.json(), sort_keys=True,
                     indent=4)  # json obj to str
    print(res)
    print('number of people: ', response.json()['number'])

    for item in response.json()['people']:
        print(item['name'])

except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
