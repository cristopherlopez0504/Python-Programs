
# This program provides basic financial advice based on user input.
# The user provides their income, debt amount, and percentage they want to save
# Based on this information, the program outputs a calculation with a breakdown of how much is saved and what is remaining.

import streamlit as st

UNDER_MAINTENANCE = False

def calculate_remainder(income_amount, debt_amount, expense_amount, savings_percentage_input):
    j = round((income_amount - debt_amount - expense_amount - (savings_percentage_input / 100 * income_amount)))
    j_formatted = f"${j:.2f}"
    return j_formatted

def calculate_future_savings(monthly_savings):
    r = 0.07 / 12
    n = 12 * 20
    z = round(monthly_savings * (((1 + r) ** n - 1) / r))
    z_formatted = f"${z:,.2f}"
    return z_formatted

#Collects user input and stores values in a dictionary

def get_user_input():
    return {
    
    'income' : st.number_input("Net Income:"),
    'savings_percentage' : st.number_input("How much of your income do you want to save?:"),
    'expenses' : st.number_input("Living Expenses: "),
    'debt' : st.number_input("Debt: ")

    }

def main():

    if UNDER_MAINTENANCE:
        st.error("### 🚧 We are currently undergoing scheduled maintenance.")
        st.write("We expect to be back online shortly. Thank you for your patience.")
        st.stop()

    user_data = get_user_input()

    #Savings Data
    savings_amount = round(float(user_data['savings_percentage'] / 100) * float(user_data['income']))
    savings_amount_formatted = f"${savings_amount:.2f}"

    #Calls calculate_remainder and users dictionary values as parameters
    remainder = calculate_remainder(user_data['income'], user_data['debt'], user_data['expenses'], user_data['savings_percentage'])
    future = calculate_future_savings(savings_amount)

    st.title("Monthly Finance Calculator", text_alignment="center") 
    st.subheader(savings_amount_formatted, text_alignment="center")
    st.subheader("Saved Monthly", text_alignment="center")
    st.write(" ")
    st.write(" ")
    st.subheader(future, text_alignment ="center")
    st.subheader("After 20 years sitting in the S&P500 (adjusted for inflation)", text_alignment="center")
    st.write(" ")
    st.write(" ")
    st.subheader(remainder, text_alignment="center")
    st.subheader("Remaining Monthly", text_alignment="center")

    
main()