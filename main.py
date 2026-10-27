from booking import RailwayBooking


def main():
    booking = RailwayBooking()
    while True:
        print("\nRailway Ticket Reservation System")
        print("1. Add booking  2. Cancel booking  3. Total fare  4. Discount  5. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                name = input("Passenger name: ").strip()
                fare = float(input("Ticket fare: "))
                booking.add_booking(name, fare)
                print("Booking added")
            elif choice == "2":
                booking.remove_booking(input("Passenger name: ").strip())
                print("Booking cancelled")
            elif choice == "3":
                print("Total fare:", booking.total_fare())
            elif choice == "4":
                discount = float(input("Discount (%): "))
                print("Discounted fare:", booking.discounted_fare(discount))
            elif choice == "5":
                break
            else:
                print("Invalid choice")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
