import requests
from flight_data import FlightData

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"

headers = {
            "apikey": "KIWI ENDPOINT API KEY",
        }
class FlightSearch:
    def get_destination_code(self, city_name):

        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query", params=parameters, headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, iata_code, destination_iata, from_time, to_time):

        parameters = {
            "fly_from": iata_code,
            "fly_to": destination_iata,
            "date_from": from_time,
            "date_to": to_time,
            "flight_type": "round",
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }

        response_4 = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=parameters)
        data = response_4.json()["data"][0]

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport=data["route"][0]["flyFrom"],
            arrival_city=data["route"][0]["cityTo"],
            arrival_airport=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.arrival_city}: £{flight_data.price} date: {flight_data.departure_date}")
        return flight_data
