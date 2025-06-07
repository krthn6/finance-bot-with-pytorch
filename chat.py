import random
import json

import torch
from users import user_database
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"
user_id = input("Hello! Please enter your user ID: ").strip()
if user_id not in user_database:
    print("Sorry! User not found. Please check again :0 ")
    exit()

user_profile = user_database[user_id]
def get_account_balance():
    name = user_profile['personal_info']['name']
    balance = user_profile['financial_info']['balance']
    spent = user_profile['financial_info']['spent_this_week']
    account_type = user_profile['financial_info']['account_type']
    return f"{name}, your current balance is ${balance:.2f}. You've spent ${spent:.2f} this week. You have a {account_type} account."

def get_user_transaction_summary(str: user_id):
    user_data = user_database.get(user_id)
    transactions = user_data['recent_transactions']
    total_spent = 0.0
    total_income = 0.0
    transaction_count = 0
    spending_by_category = {}

    for t in transactions:
        amount = t['amount']
        category = t['category']
        transaction_count += 1
        if amount < 0:
            total_spent += abs(amount)
            spending_by_category[category] = spending_by_category.get(category, 0.0) + abs(amount)
        else:
            total_income += amount
    net_change = total_income - total_spent

    return {
        "total_spent": total_spent,
        "total_income": total_income,
        "net_change": net_change,
        "transaction_count": transaction_count,
        "spending_by_category": spending_by_category
    }

def get_loan_status():
    name = user_profile['personal_info']['name']
    loan_info = user_profile['loan_info']
    status = loan_info['loan_status']
    
    if status == "approved":
        loan_amount = loan_info['loan_amount']
        monthly_payment = loan_info['monthly_payment']
        return f"Congratulations {name}, your loan of ${loan_amount:,.2f} is approved! Your monthly payment is ${monthly_payment:.2f}."
    elif status == "pending":
        loan_amount = loan_info['loan_amount']
        return f"{name}, your loan application for ${loan_amount:,.2f} is currently {status}. We'll update you soon!"
    else:
        return f"Unfortunately, {name}, your loan status is: {status}."

def get_overdue_payments():
    name = user_profile['personal_info']['name']
    payments = user_profile['overdue_payments']
    if not payments:
        return f"{name}, you have no overdue payments! Great job staying current!"
    
    lines = []
    total_overdue = 0
    for p in payments:
        lines.append(
            f"- {p['type']} payment of ${p['amount']:.2f} to {p.get('creditor', 'Unknown')}, overdue by {p['due_days_ago']} day(s)."
        )
        total_overdue += p['amount']
    
    return f"{name}, you have ${total_overdue:.2f} in overdue payments:\n" + "\n".join(lines)

def get_recent_transactions():
    name = user_profile['personal_info']['name']
    transactions = user_profile['recent_transactions'][:5]  
    if not transactions:
        return f"{name}, no recent transactions found."
    
    lines = [f"{name}, here are your recent transactions:"]
    for t in transactions:
        amount_str = f"${abs(t['amount']):.2f}"
        if t['amount'] < 0:
            lines.append(f"- {t['date']}: Spent {amount_str} at {t['merchant']} ({t['category']})")
        else:
            lines.append(f"- {t['date']}: Received {amount_str} from {t['merchant']} ({t['category']})")
    
    return "\n".join(lines)

def get_spending_summary():
    name = user_profile['personal_info']['name']
    summary = get_user_transaction_summary(user_id)
    
    top_categories = sorted(summary['spending_by_category'].items(), 
                           key=lambda x: x[1], reverse=True)[:3]
    
    response = f"{name}, here's your spending summary:\n"
    response += f"- Total spent: ${summary['total_spent']:.2f}\n"
    response += f"- Total income: ${summary['total_income']:.2f}\n"
    response += f"- Net change: ${summary['net_change']:.2f}\n"
    response += f"- Number of transactions: {summary['transaction_count']}\n"
    
    if top_categories:
        response += "\nTop spending categories:\n"
        for category, amount in top_categories:
            response += f"- {category}: ${amount:.2f}\n"
    
    return response

def get_credit_score():
    name = user_profile['personal_info']['name']
    credit_score = user_profile['financial_info']['credit_score']
    
    if credit_score >= 800:
        rating = "Excellent"
    elif credit_score >= 740:
        rating = "Very Good"
    elif credit_score >= 670:
        rating = "Good"
    elif credit_score >= 580:
        rating = "Fair"
    else:
        rating = "Poor"
    
    return f"{name}, your credit score is {credit_score} ({rating} rating)."

def get_account_info():
    name = user_profile['personal_info']['name']
    email = user_profile['personal_info']['email']
    account_type = user_profile['financial_info']['account_type']
    last_login = user_profile['account_activity']['last_login']
    
    return f"{name}, your account details:\n- Email: {email}\n- Account Type: {account_type}\n- Last Login: {last_login}"
def get_recent_activity():
    name = user_profile['personal_info']['name']
    last_login = user_profile['account_activity']['last_login']
    return f"{name}, your last login was at: {last_login}"

def get_transaction_by_category():
    summary = get_user_transaction_summary(user_id)
    name = user_profile['personal_info']['name']
    top_categories = sorted(summary['spending_by_category'].items(), 
                           key=lambda x: x[1], reverse=True)[:3]
    response_str = f"{name}, here are your top spending categories:\n"
    if top_categories:
        response_str += "\nTop spending categories:\n"
        for category, amount in top_categories:
            response_str += f"- {category}: ${amount:.2f}\n"
    
    return response_str


def get_income_info():
    monthly_income = user_profile['financial_info']['monthly_income']
    name = user_profile['personal_info']['name']
    return f"{name}, your monthly income is {monthly_income}"
def get_contact_info():
    name = user_profile['personal_info']['name']
    email = user_profile['personal_info']['email']
    phone = user_profile['personal_info']['phone']

    return f"{name}, this is the contact information we have on file. Your phone number is: {phone} and your registered email is: {email}"


print("Let's chat! (type 'quit' to exit)")
while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if tag == "account_balance":
                    response = get_account_balance()
                elif tag == "loan_status":
                    response = get_loan_status()
                elif tag == "payments_overdue":
                    response = get_overdue_payments()
                elif tag == "recent_transactions": 
                    response = get_recent_transactions()
                elif tag == "spending_summary":  
                    response = get_spending_summary()
                elif tag == "credit_score":  
                    response = get_credit_score()
                elif tag == "account_info":  
                    response = get_account_info()
                elif tag == "account_activity":
                    response = get_recent_activity()
                elif tag == "transaction_categories":
                    response = get_transaction_by_category()
                elif tag == "income_info":
                    response = get_income_info()
                elif tag == "contact_info":
                    response = get_contact_info()
                elif intent["responses"] and intent["responses"][0] != "__USE_DYNAMIC_RESPONSE__":
                    response = random.choice(intent['responses'])
                
                else:
                     response = "I'm sorry, I don't have a specific function to handle that request right now."
                break 

    print(f"{bot_name}: {response}")