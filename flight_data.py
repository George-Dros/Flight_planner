class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, departure_airport, departure_city, arrival_airport, arrival_city, departure_date, return_date):
        self.price = price
        self.departure_airport = departure_airport
        self.departure_city = departure_city
        self.arrival_airport = arrival_airport
        self.arrival_city = arrival_city
        self.departure_date = departure_date
        self.return_date = return_date


