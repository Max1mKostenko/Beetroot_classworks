import unittest
from unittest.mock import Mock
from oop_exercises.task_7 import Flight


class TestMock(unittest.TestCase):
    def setUp(self) -> None:
        self.my_flight = Flight("193F19A", "Kiev", "Los Angeles", "05:00", "14:00", 12)

    def test_average_rate(self):
        calculate_flight_duration = Mock()
        calculate_flight_duration.return_value = "The difference between 05:00 and 14:00 is " \
                                                 "9 hours and 0 minutes."
        class_variable = self.my_flight.calculate_flight_duration()
        self.assertEqual(calculate_flight_duration.return_value, class_variable)

    def test_book_seats(self):
        book_seats = Mock()
        book_seats.return_value = 12
        class_variable = self.my_flight.book_seats()
        self.assertEqual(book_seats.return_value, class_variable)


if __name__ == "__main__":
    unittest.main()
