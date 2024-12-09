# BLOOD_PRESSURE

A simple web application for recording, analyzing, and tracking blood pressure levels. Built with Python (Flask framework) and SQLite database, this project demonstrates a complete workflow of data storage, processing, and display.

---

## Features

1. **Blood Pressure Input Form**  
   - Users can input systolic (high pressure) and diastolic (low pressure) values.

2. **Real-time Blood Pressure Analysis**  
   - Determines if the entered values indicate **Normal** or **High Blood Pressure** based on standard thresholds.

3. **Data Storage and History Display**  
   - Stores all submissions in an SQLite database with timestamps.  
   - Displays a history of past records on the homepage.

---

## Technologies Used

- **Frontend**: HTML (generated dynamically via Flask templates).
- **Backend**: Python with Flask.
- **Database**: SQLite for lightweight data storage.

---

## Prerequisites

To run this project locally, ensure you have the following installed:
- Python 3.7 or later
- pip (Python package installer)

---

## Setup and Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Henry-THT/BLOOD_PRESSURE.git
   cd BLOOD_PRESSURE

	2.	Create a Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


	3.	Install Dependencies

pip install flask


	4.	Run the Application

python app.py


	5.	Access the Application
	•	Open your browser and go to: http://127.0.0.1:5000/

How It Works

	1.	Home Page
	•	Users are presented with a form to input blood pressure values (high and low).
	2.	Analysis
	•	The system checks the input values:
	•	Normal: Systolic < 140 and Diastolic < 90.
	•	High Blood Pressure: Systolic ≥ 140 or Diastolic ≥ 90.
	3.	Data Storage
	•	Each input is stored in the SQLite database along with the result and timestamp.
	4.	History
	•	A section below the form displays all previous records stored in the database.

Database Schema

The SQLite database (data.db) contains the following table:

Column	Type	Description
id	INTEGER	Primary key (auto-increment).
high_pressure	INTEGER	Systolic value (input by user).
low_pressure	INTEGER	Diastolic value (input by user).
result	TEXT	Analysis result (Normal/High).
timestamp	TEXT	Date and time of input.

Troubleshooting

Common Issues

	1.	Database Not Found
	•	Ensure the data.db file is created during the first run of the application.
	•	Check the init_db function in app.py.
	2.	Port Already in Use
	•	If 127.0.0.1:5000 is unavailable, stop any processes using that port or run the app on a different port:

python app.py --port=5001


	3.	Dependencies Not Installed
	•	Double-check your Python environment and ensure Flask is installed.

Contributing

Contributions are welcome! If you’d like to improve this project:

	1.	Fork the repository.
	2.	Create a new feature branch (git checkout -b feature-name).
	3.	Commit your changes (git commit -m "Add feature name").
	4.	Push the branch (git push origin feature-name).
	5.	Open a Pull Request.

License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code.

Contact

If you have any questions or feedback, feel free to reach out:

	•	GitHub: Henry-THT

Thank you for checking out the BLOOD_PRESSURE project!
