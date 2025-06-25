import requests
from io import BytesIO

url = "file:///C:/Users/HI/Downloads/logo.png"
response = requests.get(url)
logo = Image.open(BytesIO(response.content))
st.image(logo, width=120)

import streamlit as st

st.set_page_config(page_title="GST Calculator", page_icon="💰")

st.title("🧾 GST Calculator (India)")

st.write("Calculate GST easily without knowing any law!")

amount = st.number_input("Enter Amount (INR)", min_value=0.0, format="%.2f")
gst_rate = st.selectbox("Select GST Rate (%)", [5, 12, 18, 28])

option = st.radio("Choose Type", ["Add GST", "Remove GST"])

if st.button("Calculate"):
    if option == "Add GST":
        gst_amount = (amount * gst_rate) / 100
        total = amount + gst_amount
        st.success(f"GST Amount: ₹{gst_amount:.2f}")
        st.success(f"Total Amount (Including GST): ₹{total:.2f}")
    else:
        base_price = amount / (1 + gst_rate / 100)
        gst_amount = amount - base_price
        st.success(f"Base Price: ₹{base_price:.2f}")
        st.success(f"GST Amount Included: ₹{gst_amount:.2f}")
