import requests

SHEETY_ENDPOINT = "SHEETY URL TO YOUR GOOGLE DOCS"
headers = {"Authorization": "SHEETY AUTHORIZATION KEY",}

class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.lowest_price = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:

            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }

            put_sheety_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"

            response_3 = requests.put(url=put_sheety_endpoint, json=new_data, headers=headers)


