💰 Personal Finance Management System

A Python-based application that helps users **track income, expenses, and savings**, store financial data securely, and visualize spending patterns using charts.

---

## 📌 Project Overview

Managing personal finances is essential for effective budgeting and savings.  
This project provides a **simple and user-friendly Personal Finance Management System** that allows users to:

- Record income and expenses
- Calculate total savings
- Store data using SQLite database
- Visualize expenses using graphs

---

## 🛠 Technologies Used

- **Python** – Core programming language  
- **SQLite** – Database for data storage  
- **Tkinter** – Graphical User Interface (GUI)  
- **Matplotlib** – Data visualization (charts)

---

## ✨ Features

- ➕ Add Income records  
- ➖ Add Expense records  
- 💾 Persistent data storage using SQLite  
- 📊 Expense analysis using bar charts  
- 📈 Automatic calculation of savings  
- 🖥 Simple and intuitive GUI  

---

## 📂 Project Structure

personal-finance-manager/
│
├── finance.py # Main Python application
├── finance.db # SQLite database (auto-created)
├── README.md # Project documentation

yaml
Copy code

---

## 🧠 Database Design

**Table Name:** `transactions`

| Column   | Data Type |
|--------|----------|
| id      | INTEGER (Primary Key) |
| type    | TEXT (Income / Expense) |
| category| TEXT |
| amount  | REAL |
| date    | TEXT |

---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-finance-manager.git
Navigate to the project folder:

bash
Copy code
cd personal-finance-manager
Install required library:

bash
Copy code
pip install matplotlib
Run the application:

bash
Copy code
python finance.py
📊 Output
GUI for entering income and expenses

Summary showing:

Total Income

Total Expense

Savings

Bar chart displaying category-wise expenses

🗣 Project Explanation (For Viva)
This Personal Finance Management System is developed using Python and SQLite.
It allows users to manage income and expenses, calculates savings automatically, stores data persistently, and visualizes expense data using Matplotlib charts. Tkinter is used to provide a simple graphical interface.

🚀 Future Enhancements
Monthly and yearly financial reports

User authentication system

Export data to Excel

Pie chart visualization

Web-based version using Flask

👩‍💻 Author
Anshika Chauhan
Maharaja Agrasen Institute Of Technology


yaml
Copy code
