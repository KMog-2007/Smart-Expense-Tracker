# 💰 Smart Expense Tracker

A simple and user-friendly web application built with Python and Flask to manage personal income and expenses.

## 📌 Project Overview

Smart Expense Tracker is a web-based personal finance management application. It allows users to record income and expenses, monitor their balance, analyze spending habits, search and filter transactions, view monthly summaries, visualize expenses, and export transaction data.

## ✨ Features

- 💵 Add income and expense transactions
- 💰 Automatically calculate total income
- 💸 Automatically calculate total expenses
- 🧮 Automatically calculate current balance
- ✏️ Edit transactions
- 🗑️ Delete transactions
- 🔎 Search transactions
- 🔍 Filter by category, transaction type, and date
- 📅 View monthly expense summaries
- 📊 View expense insights
- 📈 Visualize spending using a doughnut chart
- 📥 Export transactions to CSV
- ✅ Input validation
- 📱 Responsive user interface

## 📊 Expense Insights

The application provides useful spending information including:

- Total number of expenses
- Average expense
- Highest spending category
- Highest category spending amount
- Percentage of expenses spent in the highest category
- Automatic spending insight

## 🛠️ Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- JavaScript
- Chart.js
- Visual Studio Code
- Git
- GitHub

## 🏗️ Project Structure

Smart Expense Tracker/
├── app.py
├── database.py
├── models.py
├── utils.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── database/
│   └── expenses.db
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css

## 📂 File Description

### app.py

Main Flask application containing:

- Flask routes
- Adding transactions
- Editing transactions
- Deleting transactions
- Searching and filtering
- Expense calculations
- Monthly summaries
- Expense insights
- CSV export
- Input validation

### database.py

Handles:

- SQLite configuration
- SQLAlchemy initialization
- Database folder creation
- Database initialization

### models.py

Defines the Transaction database model containing:

- ID
- Transaction type
- Amount
- Category
- Description
- Date

### utils.py

Contains utility functions used by the project.

### templates/index.html

Main dashboard interface containing:

- Dashboard cards
- Add transaction form
- Expense insights
- Search and filters
- Monthly summary
- Spending chart
- Transaction history
- CSV export

### templates/edit.html

Provides the interface for editing existing transactions.

### static/style.css

Contains the complete styling and responsive design for the application.

### requirements.txt

Contains the Python packages required to run the project.

### .gitignore

Prevents unnecessary files such as the virtual environment, Python cache files, database files, and IDE files from being uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

Replace YOUR_GITHUB_REPOSITORY_URL with your GitHub repository URL.

    git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project folder

    cd Smart-Expense-Tracker

### 3. Create a virtual environment

    python -m venv venv

### 4. Activate the virtual environment

Windows:

    venv\Scripts\activate

macOS/Linux:

    source venv/bin/activate

### 5. Install dependencies

    pip install -r requirements.txt

### 6. Run the application

    python app.py

### 7. Open in browser

    http://127.0.0.1:5000

## 🚀 How to Use

### Add a Transaction

Enter:

- Transaction type
- Amount
- Category
- Description
- Date

Then click Add Transaction.

### View Dashboard

The dashboard displays:

- Total Balance
- Total Income
- Total Expenses
- Total Transactions

### Analyze Expenses

The Expense Insights section displays:

- Total expenses
- Average expense
- Highest spending category
- Category percentage
- Spending insight

### Search and Filter

Transactions can be searched and filtered using:

- Description
- Category
- Transaction type
- Date

### Monthly Summary

Select a month to view:

- Total monthly expenses
- Number of expenses
- Category-wise spending

### Edit a Transaction

Click Edit in the transaction history, update the information, and save the changes.

### Delete a Transaction

Click Delete and confirm the deletion.

### Export Transactions

Click Export Transactions to CSV to download all transaction records as expenses.csv.

## 🔄 CRUD Operations

The application implements all major CRUD operations.

### Create

Add new income and expense transactions.

### Read

View transactions and financial summaries.

### Update

Edit existing transactions.

### Delete

Remove transactions from the database.

## 🗄️ Database

The application uses SQLite with Flask-SQLAlchemy.

Each transaction contains:

- ID
- Transaction Type
- Amount
- Category
- Description
- Date

The database is automatically initialized when the application starts.

## ✅ Input Validation

The application validates user input before storing data.

Examples:

- Transaction type must be Income or Expense
- Amount must be greater than ₹0
- Category cannot be empty
- Date cannot be empty
- Date must be valid
- Invalid amounts are rejected

## 📈 Data Visualization

The application uses Chart.js to display expense distribution by category through a doughnut chart.

This makes it easier to understand which categories contribute most to overall expenses.

## 📥 CSV Export

The CSV export feature generates a file containing:

- ID
- Type
- Amount
- Category
- Description
- Date

The exported file can be opened using:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Other spreadsheet applications

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python programming
- Flask web development
- Flask routing
- HTML forms
- Jinja templates
- CSS
- JavaScript
- SQLAlchemy ORM
- SQLite databases
- CRUD operations
- Form validation
- Error handling
- Searching and filtering
- Data aggregation
- Expense analysis
- Data visualization
- CSV generation
- Virtual environments
- Git
- GitHub

## 🔮 Future Improvements

Possible future improvements include:

- User registration and login
- Password authentication
- Multiple user accounts
- Personal budget management
- Monthly budget limits
- Budget alerts
- Recurring transactions
- PDF reports
- Advanced financial analytics
- Spending trend analysis
- Expense forecasting
- Cloud database integration
- Mobile application
- Progressive Web App support
- Cloud deployment

## 📸 Screenshots

Screenshots of the application can be added here.

### Dashboard

Add the dashboard screenshot here.

### Expense Insights

Add the expense insights screenshot here.

### Transaction History

Add the transaction history screenshot here.

### Monthly Expense Summary

Add the monthly summary screenshot here.

## 📌 Project Highlights

This project combines:

Python + Flask + SQLite + SQLAlchemy + HTML + CSS + JavaScript + Chart.js

to create a complete personal expense management web application.

## 👨‍💻 Project Type

Python Flask Capstone Project

## 📄 License

This project is created for educational and portfolio purposes.