import pytest
from unittest.mock import Mock
from booking import RailwayBooking

@pytest.fixture
def booking():
    return RailwayBooking()

def test_add_booking(booking):
    booking.add_booking("Passenger1", 500)
    assert booking.total_fare() == 500

def test_multiple_bookings(booking):
    booking.add_booking("Passenger1", 500)
    booking.add_booking("Passenger2", 300)
    assert booking.total_fare() == 800

def test_remove_booking(booking):
    booking.add_booking("Passenger1", 500)
    booking.remove_booking("Passenger1")
    assert booking.total_fare() == 0

def test_discount(booking):
    booking.add_booking("Passenger1", 1000)
    assert booking.discounted_fare(10) == 900

def test_empty_booking(booking):
    assert booking.total_fare() == 0

def test_zero_fare(booking):
    with pytest.raises(ValueError):
        booking.add_booking("Passenger1", 0)

def test_negative_fare(booking):
    with pytest.raises(ValueError):
        booking.add_booking("Passenger1", -100)

def test_empty_name(booking):
    with pytest.raises(ValueError):
        booking.add_booking("", 500)

def test_invalid_discount(booking):
    booking.add_booking("Passenger1", 1000)
    with pytest.raises(ValueError):
        booking.discounted_fare(101)

def test_negative_discount(booking):
    booking.add_booking("Passenger1", 1000)
    with pytest.raises(ValueError):
        booking.discounted_fare(-1)

def test_remove_missing_booking(booking):
    with pytest.raises(ValueError):
        booking.remove_booking("Unknown")

def test_minimum_valid_fare(booking):
    booking.add_booking("Passenger1", 0.01)
    assert booking.total_fare() == 0.01

def test_zero_discount(booking):
    booking.add_booking("Passenger1", 1000)
    assert booking.discounted_fare(0) == 1000

def test_maximum_discount(booking):
    booking.add_booking("Passenger1", 1000)
    assert booking.discounted_fare(100) == 0

def test_booking_notification():
    notifier = Mock()
    booking = RailwayBooking(notifier=notifier)
    booking.add_booking("Passenger1", 500)
    notifier.send.assert_called_once_with("Passenger1")
