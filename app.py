import streamlit as st

st.set_page_config(page_title="Bank App", page_icon="🏦", layout="wide")

# ------------------ BANK CLASS ------------------

class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdraw Successful: ₹{amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful: ₹{amount}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile Updated: {self.mobile_number}"

    def check_balance(self):
        return self.balance


# ------------------ TITLE ------------------

st.title("🏦 SBI Banking Dashboard")
st.write("Simple Banking Application built with Streamlit")

# ------------------ SIDEBAR ------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select Option",
    ["Create Account", "Deposit", "Withdraw", "Check Balance", "Update Mobile"]
)

# ------------------ CREATE ACCOUNT ------------------

if menu == "Create Account":

    st.subheader("Create New Bank Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        account_number = st.text_input("Account Number")
        age = st.number_input("Age", min_value=18)

    with col2:
        mobile = st.text_input("Mobile Number")
        balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):

        st.session_state.account = BankApplication(
            name, account_number, age, mobile, balance
        )

        st.success("Account Created Successfully")

# ------------------ DEPOSIT ------------------

elif menu == "Deposit":

    st.subheader("Deposit Money")

    amount = st.number_input("Enter Amount")

    if st.button("Deposit"):

        result = st.session_state.account.deposit(amount)

        st.success(result)

# ------------------ WITHDRAW ------------------

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    amount = st.number_input("Enter Amount")

    if st.button("Withdraw"):

        result = st.session_state.account.withdraw(amount)

        st.success(result)

# ------------------ CHECK BALANCE ------------------

elif menu == "Check Balance":

    st.subheader("Account Balance")

    balance = st.session_state.account.check_balance()

    st.metric("Current Balance", f"₹{balance}")

# ------------------ UPDATE MOBILE ------------------

elif menu == "Update Mobile":

    st.subheader("Update Mobile Number")

    new_mobile = st.text_input("Enter New Mobile Number")

    if st.button("Update"):

        result = st.session_state.account.update_mobile(new_mobile)

        st.success(result)