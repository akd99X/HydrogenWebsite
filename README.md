# Hydrogen Fuel Cell Calculator

A web application developed by me to calculate hydrogen-to-power conversions, task-based hydrogen needs, and compare the CO₂ emissions and costs of different hydrogen production methods.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Team Members & Contributions](#team-members--contributions)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Project Overview
I developed the Hydrogen Fuel Cell Calculator to:
- Estimate hydrogen-to-power conversions for various applications.
- Determine hydrogen requirements for specific tasks like vehicle charging.
- Compare CO₂ emissions and costs between Green, Gray, and Blue Hydrogen.

This tool is designed to help researchers, businesses, and engineers make data-driven decisions in the hydrogen fuel industry. The calculator provides real-time, scientifically-backed estimations to promote clean energy adoption.

---

## Features
- **Hydrogen ↔ Power Calculator** – Convert hydrogen mass to power and vice versa.
- **Task-Based Estimator** – Calculate hydrogen needs for real-world tasks (e.g., charging cars).
- **Production Method Comparison** – Compare cost and CO₂ impact of Green, Gray, and Blue Hydrogen.
- **User-Friendly Interface** – Simple, intuitive UI with interactive calculations.

---

## Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (Expandable if needed)
- **Testing & Documentation:** Pytest, Markdown

---

## Team Members & Contributions

| Name           | Role                   | Contributions                                       |
|---------------|------------------------|-----------------------------------------------------|
| **Iskandar Kafi**  | Full-Stack Developer   | Designed and developed the entire Flask backend.  |
|               |                        | Created API routes and implemented power calculations.  |
|               |                        | Built an intuitive UI for the calculator.  |
|               |                        | Managed database structure and integrations.  |
| **Zeina Kotb** | Testing & Documentation | Conducted unit tests and debugging.  |
|               |                        | Wrote technical documentation.  |
|               |                        | Verified accuracy in hydrogen production comparisons.  |
|               |                        | Improved performance and optimized calculations.  |

---

## Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/zeinakotb/HydrogenWebsite.git
cd HydrogenWebsite
Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run the Application
bash
Copy
Edit
flask run
The app will be available at: http://127.0.0.1:5000/

Usage
Open the application in a browser.

Enter hydrogen values or power requirements.

Use the task-based estimator to determine hydrogen needs for real-world applications.

Compare hydrogen production methods to evaluate efficiency and environmental impact.

API Endpoints
Your app provides multiple API routes for backend calculations. Here’s how they work:

Hydrogen to Power Calculation
Endpoint: /calculate_power

Method: POST

Request Body:

json
Copy
Edit
{ "hydrogen": 500 }
Response:

json
Copy
Edit
{ "power": 16.65 }
Power to Hydrogen Calculation
Endpoint: /calculate_hydrogen

Method: POST

Request Body:

json
Copy
Edit
{ "power": 100 }
Response:

json
Copy
Edit
{ "hydrogen": 3.0 }
Task-Based Hydrogen Estimation
Endpoint: /convert_task

Method: POST

Request Body:

json
Copy
Edit
{ "task": "charge 5 cars" }
Response:

json
Copy
Edit
{ "hydrogen": 7.51 }
Hydrogen Production Method Comparison
Endpoint: /compare_methods

Method: POST

Request Body:

json
Copy
Edit
{ "method": "green" }
Response:

json
Copy
Edit
{ "cost": 5, "co2": 0 }
Future Enhancements
Real-time Hydrogen Cost Tracking – Fetch live prices for Green, Gray, and Blue Hydrogen.

API Integration – Allow third-party apps to use our calculations.

Expanded Task-Based Calculations – Support more use cases (e.g., industrial hydrogen consumption).

Improved UX/UI – Enhance visuals and interactive elements for better user experience.

License
This project is licensed under the MIT License. See the LICENSE file for details.

sql
Copy
Edit

Now **copy and paste** this into your `README.md` file, commit it, and push it to **GitHub**. 🚀 Let me know if you need any last-minute edits!






