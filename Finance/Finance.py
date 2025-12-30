
import streamlit as st

st.title("Monthly Finance Calculator", text_alignment="center")


# This program provides basic financial advice based on user input.
# The user provides their income, debt amount, and percentage they want to save
# Based on this information, the program outputs a calculation with a breakdown of how much is saved and what is remaining.

#Function user 4 parameters to calculate the amount of money left over
def calculate_net(income_amount, debt_amount, expense_amount, savings_percentage_input): 
    j = round((income_amount - debt_amount - expense_amount - (savings_percentage_input * income_amount)))
    j_formatted = f"${j:.2f}"
    return j_formatted

def future_savings(monthly_savings):
    r = 0.07 / 12
    n = 12 * 20
    z = round(monthly_savings * (((1 + r) ** n - 1) / r))
    z_formatted = f"${z:,.2f}"
    return z_formatted

#Collects user input
user_income_input = st.number_input('Net Income:')
savings_percentage_input = st.number_input(f"How much of your income do you want to save? (percent as a decmial):")
user_expenses_input = st.number_input("\nLiving Expenses: ")
user_debt_input = st.number_input("\nDebt: ")


#Savings Data
savings_amount = round(float(savings_percentage_input) * float(user_income_input))
savings_amount_formatted = f"${savings_amount:.2f}"

#Call the calculate_net function and users users input as the parameters
remainder = calculate_net(user_income_input, user_debt_input, user_expenses_input, savings_percentage_input)
future = future_savings(savings_amount)

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