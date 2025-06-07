import random
from datetime import datetime, timedelta
from typing import Dict, List, Any

user_database = {
    "alex456": {
        "personal_info": {
            "name": "Alex",
            "email": "alex456@email.com",
            "phone": "+1-555-0123",
            "age": 28,
            "registration_date": "2023-01-15"
        },
        "financial_info": {
            "balance": 7845.10,
            "spent_this_week": 984.00,
            "credit_score": 742,
            "account_type": "Premium",
            "monthly_income": 6500.00,
            "debt_to_income_ratio": 0.23
        },
        "loan_info": {
            "loan_status": "approved",
            "loan_amount": 25000.00,
            "loan_type": "Personal",
            "interest_rate": 7.5,
            "monthly_payment": 485.50
        },
        "overdue_payments": [],
        "recent_transactions": [
            {"date": "2025-06-06", "type": "Purchase", "category": "Groceries", "amount": -127.50, "merchant": "Whole Foods"},
            {"date": "2025-06-05", "type": "Purchase", "category": "Gas", "amount": -65.00, "merchant": "Shell Station"},
            {"date": "2025-06-04", "type": "Transfer", "category": "Income", "amount": 2500.00, "merchant": "Salary Deposit"},
            {"date": "2025-06-03", "type": "Purchase", "category": "Entertainment", "amount": -89.99, "merchant": "Netflix"},
            {"date": "2025-06-02", "type": "Purchase", "category": "Dining", "amount": -45.75, "merchant": "Pizza Palace"},
            {"date": "2025-06-01", "type": "Purchase", "category": "Shopping", "amount": -234.99, "merchant": "Amazon"},
            {"date": "2025-05-31", "type": "ATM", "category": "Cash", "amount": -100.00, "merchant": "Bank ATM"},
            {"date": "2025-05-30", "type": "Purchase", "category": "Utilities", "amount": -145.30, "merchant": "Electric Company"},
            {"date": "2025-05-29", "type": "Purchase", "category": "Healthcare", "amount": -75.00, "merchant": "CVS Pharmacy"},
            {"date": "2025-05-28", "type": "Purchase", "category": "Transportation", "amount": -55.25, "merchant": "Uber"}
        ],
        "account_activity": {
            "last_login": "2025-06-07",
            "login_frequency": "Daily",
            "app_version": "2.1.4",
            "device_type": "Mobile"
        }
    },
    "jamie12": {
        "personal_info": {
            "name": "Jamie",
            "email": "jamie12@email.com",
            "phone": "+1-555-0124",
            "age": 31,
            "registration_date": "2022-08-22"
        },
        "financial_info": {
            "balance": 1920.45,
            "spent_this_week": 310.22,
            "credit_score": 678,
            "account_type": "Standard",
            "monthly_income": 4200.00,
            "debt_to_income_ratio": 0.31
        },
        "loan_info": {
            "loan_status": "under review",
            "loan_amount": 15000.00,
            "loan_type": "Auto",
            "interest_rate": 8.2,
            "monthly_payment": 0.00
        },
        "overdue_payments": [],
        "recent_transactions": [
            {"date": "2025-06-06", "type": "Purchase", "category": "Groceries", "amount": -85.40, "merchant": "Safeway"},
            {"date": "2025-06-05", "type": "Purchase", "category": "Coffee", "amount": -12.50, "merchant": "Starbucks"},
            {"date": "2025-06-04", "type": "Purchase", "category": "Gas", "amount": -50.75, "merchant": "Chevron"},
            {"date": "2025-06-03", "type": "Transfer", "category": "Income", "amount": 1400.00, "merchant": "Payroll"},
            {"date": "2025-06-02", "type": "Purchase", "category": "Dining", "amount": -32.99, "merchant": "Chipotle"},
            {"date": "2025-06-01", "type": "Purchase", "category": "Subscription", "amount": -15.99, "merchant": "Spotify"},
            {"date": "2025-05-31", "type": "Purchase", "category": "Shopping", "amount": -78.25, "merchant": "Target"},
            {"date": "2025-05-30", "type": "ATM", "category": "Cash", "amount": -60.00, "merchant": "Chase ATM"},
            {"date": "2025-05-29", "type": "Purchase", "category": "Healthcare", "amount": -25.50, "merchant": "Walgreens"},
            {"date": "2025-05-28", "type": "Purchase", "category": "Transportation", "amount": -18.75, "merchant": "Metro Card"}
        ],
        "account_activity": {
            "last_login": "2025-06-06",
            "login_frequency": "Weekly",
            "app_version": "2.1.3",
            "device_type": "Desktop"
        }
    },
    "morgan87": {
        "personal_info": {
            "name": "Morgan",
            "email": "morgan87@email.com",
            "phone": "+1-555-0125",
            "age": 26,
            "registration_date": "2023-11-05"
        },
        "financial_info": {
            "balance": 563.20,
            "spent_this_week": 120.90,
            "credit_score": 598,
            "account_type": "Basic",
            "monthly_income": 3200.00,
            "debt_to_income_ratio": 0.45
        },
        "loan_info": {
            "loan_status": "rejected",
            "loan_amount": 0.00,
            "loan_type": "Personal",
            "interest_rate": 0.0,
            "monthly_payment": 0.00
        },
        "overdue_payments": [
            {"type": "Credit Card", "amount": 230.00, "due_days_ago": 4, "creditor": "Chase Bank"}
        ],
        "recent_transactions": [
            {"date": "2025-06-06", "type": "Purchase", "category": "Groceries", "amount": -45.20, "merchant": "Aldi"},
            {"date": "2025-06-05", "type": "Purchase", "category": "Fast Food", "amount": -8.99, "merchant": "McDonald's"},
            {"date": "2025-06-04", "type": "Purchase", "category": "Gas", "amount": -35.50, "merchant": "BP Station"},
            {"date": "2025-06-03", "type": "Transfer", "category": "Income", "amount": 800.00, "merchant": "Part-time Job"},
            {"date": "2025-06-02", "type": "Purchase", "category": "Utilities", "amount": -120.00, "merchant": "Phone Bill"},
            {"date": "2025-06-01", "type": "ATM", "category": "Cash", "amount": -40.00, "merchant": "ATM Fee"},
            {"date": "2025-05-31", "type": "Purchase", "category": "Shopping", "amount": -25.75, "merchant": "Dollar Store"},
            {"date": "2025-05-30", "type": "Purchase", "category": "Transportation", "amount": -15.00, "merchant": "Bus Pass"},
            {"date": "2025-05-29", "type": "Purchase", "category": "Coffee", "amount": -4.50, "merchant": "Local Cafe"},
            {"date": "2025-05-28", "type": "Purchase", "category": "Groceries", "amount": -32.80, "merchant": "Walmart"}
        ],
        "account_activity": {
            "last_login": "2025-06-05",
            "login_frequency": "Occasionally",
            "app_version": "2.0.8",
            "device_type": "Mobile"
        }
    },
    "nina99": {
        "personal_info": {
            "name": "Nina",
            "email": "nina99@email.com",
            "phone": "+1-555-0126",
            "age": 34,
            "registration_date": "2022-03-12"
        },
        "financial_info": {
            "balance": 2403.10,
            "spent_this_week": 445.00,
            "credit_score": 756,
            "account_type": "Premium",
            "monthly_income": 5800.00,
            "debt_to_income_ratio": 0.28
        },
        "loan_info": {
            "loan_status": "approved",
            "loan_amount": 30000.00,
            "loan_type": "Home Improvement",
            "interest_rate": 6.8,
            "monthly_payment": 520.75
        },
        "overdue_payments": [],
        "recent_transactions": [
            {"date": "2025-06-06", "type": "Purchase", "category": "Home Improvement", "amount": -299.99, "merchant": "Home Depot"},
            {"date": "2025-06-05", "type": "Purchase", "category": "Groceries", "amount": -156.75, "merchant": "Trader Joe's"},
            {"date": "2025-06-04", "type": "Transfer", "category": "Income", "amount": 2900.00, "merchant": "Salary"},
            {"date": "2025-06-03", "type": "Purchase", "category": "Dining", "amount": -67.50, "merchant": "Italian Restaurant"},
            {"date": "2025-06-02", "type": "Purchase", "category": "Entertainment", "amount": -45.00, "merchant": "Movie Theater"},
            {"date": "2025-06-01", "type": "Purchase", "category": "Gas", "amount": -58.25, "merchant": "Texaco"},
            {"date": "2025-05-31", "type": "Purchase", "category": "Shopping", "amount": -125.99, "merchant": "Nordstrom"},
            {"date": "2025-05-30", "type": "Purchase", "category": "Healthcare", "amount": -89.00, "merchant": "Dentist"},
            {"date": "2025-05-29", "type": "ATM", "category": "Cash", "amount": -80.00, "merchant": "Bank ATM"},
            {"date": "2025-05-28", "type": "Purchase", "category": "Subscription", "amount": -12.99, "merchant": "Disney+"}
        ],
        "account_activity": {
            "last_login": "2025-06-07",
            "login_frequency": "Daily",
            "app_version": "2.1.4",
            "device_type": "Mobile"
        }
    },
    "liam321": {
        "personal_info": {
            "name": "Liam",
            "email": "liam321@email.com",
            "phone": "+1-555-0127",
            "age": 29,
            "registration_date": "2021-12-08"
        },
        "financial_info": {
            "balance": 10984.70,
            "spent_this_week": 678.12,
            "credit_score": 812,
            "account_type": "VIP",
            "monthly_income": 8500.00,
            "debt_to_income_ratio": 0.18
        },
        "loan_info": {
            "loan_status": "pending",
            "loan_amount": 50000.00,
            "loan_type": "Investment",
            "interest_rate": 5.9,
            "monthly_payment": 0.00
        },
        "overdue_payments": [],
        "recent_transactions": [
            {"date": "2025-06-06", "type": "Investment", "category": "Stocks", "amount": -2500.00, "merchant": "E*TRADE"},
            {"date": "2025-06-05", "type": "Purchase", "category": "Dining", "amount": -125.75, "merchant": "Fine Dining"},
            {"date": "2025-06-04", "type": "Transfer", "category": "Income", "amount": 4250.00, "merchant": "Salary"},
            {"date": "2025-06-03", "type": "Purchase", "category": "Shopping", "amount": -450.99, "merchant": "Apple Store"},
            {"date": "2025-06-02", "type": "Purchase", "category": "Travel", "amount": -289.50, "merchant": "Hotel Booking"},
            {"date": "2025-06-01", "type": "Purchase", "category": "Gas", "amount": -75.25, "merchant": "Premium Shell"},
            {"date": "2025-05-31", "type": "Purchase", "category": "Groceries", "amount": -198.40, "merchant": "Whole Foods"},
            {"date": "2025-05-30", "type": "Purchase", "category": "Entertainment", "amount": -89.99, "merchant": "Concert Tickets"},
            {"date": "2025-05-29", "type": "Transfer", "category": "Savings", "amount": -1000.00, "merchant": "High Yield Savings"},
            {"date": "2025-05-28", "type": "Purchase", "category": "Healthcare", "amount": -150.00, "merchant": "Specialist Visit"}
        ],
        "account_activity": {
            "last_login": "2025-06-07",
            "login_frequency": "Daily",
            "app_version": "2.1.4",
            "device_type": "Desktop"
        }
    }
}


    
   