from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

IATA_CODE = "CITY IATA CODE"
tomorrow = datetime.now() + timedelta(1)
tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")

six_months = datetime.now() + timedelta(180)
six_months_formatted = six_months.strftime("%d/%m/%Y")


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()


for entry in sheet_data:
    if entry["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        entry["iataCode"] = flight_search.get_destination_code(entry["city"])


data_manager.destination_data = sheet_data
data_manager.update_destination_data()

check_flights = FlightSearch()

for entry in sheet_data:
    flight = check_flights.check_flights(IATA_CODE, entry["iataCode"], tomorrow_formatted, six_months_formatted)

    if flight.price < entry["lowestPrice"]:
        notification_manager.send_sms(message=f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport} to {flight.arrival_city}-{flight.arrival_airport}, from {flight.departure_date} to {flight.return_date}.")







