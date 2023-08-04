from datetime import datetime


class Flight:
    def __init__(self, flight_number, departure_city, destination_city, departure_time, arrival_time, available_seats):
        self._flight_number = flight_number
        self.departure_city = departure_city
        self.destination_city = destination_city
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self.__available_seats = available_seats

    def display_info(self):
        return f"Flight number: {self._flight_number}" \
               f"\nDeparture city: {self.departure_city}" \
               f"\nDestination city: {self.destination_city}" \
               f"\nDeparture time: {self._departure_time}" \
               f"\nArrival time: {self._arrival_time}" \
               f"\nAvailable quantity of seats: {self.__available_seats}\n"

    def seat_availability(self):
        return self.__available_seats

    def book_seats(self):
        return self.__available_seats - 1

    def calculate_flight_duration(self):
        time1 = datetime.strptime(self._departure_time, '%H:%M')
        time2 = datetime.strptime(self._arrival_time, '%H:%M')
        result = time2 - time1
        hours, minutes, sec = str(result).split(":")
        return f"The difference between {self._departure_time} and {self._arrival_time} is " \
               f"{int(hours)} hours and {int(minutes)} minutes."


my_flight = Flight("193F19A", "Kiev", "Los Angeles", "05:00", "14:00", 12)
print(my_flight.calculate_flight_duration())
print(my_flight.display_info())
