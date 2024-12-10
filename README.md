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

## Setup and Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository  
   ```bash
   git clone https://github.com/Henry-THT/BLOOD_PRESSURE.git
   cd BLOOD_PRESSURE
   ```

### 2. Create a Virtual Environment  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

### 3. Install Dependencies  
   ```bash
   pip install flask
   ```

### 4. Run the Application  
   ```bash
   python app.py
   ```

### 5. Access the Application  
   - Open your browser and go to: `http://127.0.0.1:5000/`

---

## Code Creation Thoughts

This project was created as part of a Python course assignment. The main objective was to demonstrate the use of Python and Flask in building a simple web application with a database for persistent data storage. Below are the main steps and thoughts behind the code design:

### **1. Identifying Core Features**
- The application needed to allow users to input blood pressure values, analyze them, and store the data.
- A history feature was included to make the application more practical by allowing users to review their previous records.

### **2. Technology Choices**
- **Flask**: Chosen for its simplicity and lightweight nature, making it ideal for a small web application.
- **SQLite**: Used for data storage because it is easy to set up and doesn't require a separate database server.
- **HTML (via Flask templates)**: Used for dynamic front-end content generation to keep the project simple and functional.

### **3. Code Design Approach**
1. **Database Layer**:
   - Created an SQLite database to store user inputs along with timestamps and the evaluation result.
   - Used a single table with fields for systolic pressure, diastolic pressure, result, and timestamp.
2. **Routing and Logic Layer**:
   - Designed two routes:
     - `/`: Displays the form and history records.
     - `/submit`: Processes user inputs, evaluates the data, and stores the results in the database.
   - Used a helper function to encapsulate the logic for determining whether the blood pressure is normal or high.
3. **Dynamic Frontend**:
   - Implemented a simple form using Flask's `render_template_string` to allow users to input their blood pressure values.
   - Dynamically generated history records below the form for better user interaction.

### **4. Learning Objectives**
- Understand how to use Flask to handle routing and HTTP requests.
- Learn how to interact with an SQLite database to perform basic CRUD operations.
- Practice dynamic content rendering using Flask templates.
- Handle user inputs securely and return meaningful results.

---

## Code Explanation

### **Database Setup**
- The database is initialized with a single table for storing blood pressure records. It includes:
  - `id`: Primary key.
  - `high_pressure` and `low_pressure`: Inputs from the user.
  - `result`: Analysis result.
  - `timestamp`: Time when the record was created.

### **Blood Pressure Analysis**
- Blood pressure is categorized as **Normal** or **High Blood Pressure** based on:
  - Systolic (high) pressure >= 140 or
  - Diastolic (low) pressure >= 90.

### **Routes and Logic**
1. **Home (`/`)**:
   - Displays a form for inputting blood pressure values.
   - Retrieves and displays all past records from the database.
2. **Submit (`/submit`)**:
   - Processes user inputs, performs the blood pressure analysis, and saves the results to the database.
   - Returns a result page with the analysis and a link to go back.

### **Frontend Design**
- A minimal form is dynamically generated for user inputs.
- History records are displayed below the form to enhance user experience.

---

## Database Schema

The SQLite database (`data.db`) contains the following table:

| Column         | Type     | Description                         |  
|----------------|----------|-------------------------------------|  
| `id`           | INTEGER  | Primary key (auto-increment).       |  
| `high_pressure`| INTEGER  | Systolic value (input by user).     |  
| `low_pressure` | INTEGER  | Diastolic value (input by user).    |  
| `result`       | TEXT     | Analysis result (Normal/High).      |  
| `timestamp`    | TEXT     | Date and time of input.             |  

---

## Troubleshooting

### Common Issues

1. **Database Not Found**  
   - Ensure the `data.db` file is created during the first run of the application.  
   - Check the `init_db` function in `app.py`.

2. **Port Already in Use**  
   - If `127.0.0.1:5000` is unavailable, stop any processes using that port or run the app on a different port:  
     ```bash
     python app.py --port=5001
     ```

3. **Dependencies Not Installed**  
   - Double-check your Python environment and ensure Flask is installed.

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.  
2. Create a new feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add feature name"`).  
4. Push the branch (`git push origin feature-name`).  
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code.

---

## Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [Henry-THT](https://github.com/Henry-THT)

---

Thank you for checking out the **BLOOD_PRESSURE** project!
