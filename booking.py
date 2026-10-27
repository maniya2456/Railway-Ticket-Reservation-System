"""Small railway ticket booking module for Practicals 7 and 8."""

class RailwayBooking:
    def __init__(self, notifier=None):
        self.bookings = {}
        self.notifier = notifier

    def add_booking(self, name, fare):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Passenger name required")
        if not isinstance(fare, (int, float)) or isinstance(fare, bool) or fare <= 0:
            raise ValueError("Fare must be positive")
        self.bookings[name] = fare
        if self.notifier:
            self.notifier.send(name)

    def remove_booking(self, name):
        if name not in self.bookings:
            raise ValueError("Booking not found")
        del self.bookings[name]

    def total_fare(self):
        return sum(self.bookings.values())

    def discounted_fare(self, discount):
        if not isinstance(discount, (int, float)) or not 0 <= discount <= 100:
            raise ValueError("Invalid discount")
        return self.total_fare() * (1 - discount / 100)
