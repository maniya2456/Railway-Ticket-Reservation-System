# Railway Ticket Reservation System

Student project for Software Engineering and Agile Lab Practicals 2–8.

## Features in this demonstration
- Python CLI for adding and cancelling passenger bookings
- Fare total and percentage discount calculations
- Simple HTML login skeleton (not connected to an authentication server)
- pytest automated unit tests, boundary cases, exceptions, and mock notification test

## Setup
```bash
python -m pip install -r requirements.txt
python main.py
python -m pytest -v
python -m pytest --cov=booking --cov-report=term-missing
```

## Practical documents
Place your own SRS, UML, Scrum backlog, and user-story documents in `docs/`.

This is a lab demonstration, not a production railway reservation or payment system.
