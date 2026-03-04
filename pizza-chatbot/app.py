import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from agent.pizza_agent import chat_with_agent
from data.menu import get_menu_text
from utils.bill_calculator import calculate_bill, format_bill
from utils.qr_generator import generate_upi_qr, qr_to_bytes
from PIL import Image
import io
import random


# Page Config
st.set_page_config(
    page_title="Yummy Pizza",
    page_icon=Image.open(os.path.join("assets", "yummy_piza_logo.png")),
    layout="centered"
)

#  CSS 
st.markdown("""
<style>
    .main { background-color: #fff8f0; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    h1 { color: #e76f51; text-align: center; }
    .bill-box {
        background: #1a1a2e;
        color: #f9c74f;
        padding: 16px;
        border-radius: 12px;
        font-family: monospace;
        white-space: pre-wrap;
    }
    .status-badge {
        background: #2d6a4f;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 6px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header 
st.markdown("# 🍕 Yummy Pizza")
st.markdown("<p style='text-align:center; color:#6c757d;'>Your AI pizza ordering assistant</p>", unsafe_allow_html=True)
st.divider()

# Session State Init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "app_stage" not in st.session_state:
    st.session_state.app_stage = "chatting"   # chatting | bill | payment | confirmed
if "bill" not in st.session_state:
    st.session_state.bill = None
if "order_items" not in st.session_state:
    st.session_state.order_items = []
if "greeted" not in st.session_state:
    st.session_state.greeted = False

# Auto Greeting
if not st.session_state.greeted:
    greeting = (
        "👋 Welcome to **Yummy Pizza**! I'm here to help you ordering a pizza, get the delivery in just 15 minutes.\n\n"
        "🍕 Type **'menu'** to see our full menu, or just tell me what you'd like!\n\n"
        "We have pizzas, sides & drinks — all freshly made! 😋"
    )
    st.session_state.chat_history.append({"role": "assistant", "content": greeting})
    st.session_state.greeted = True

# Sidebar
with st.sidebar:
    st.markdown("## 🍕 Quick Menu")
    st.markdown(get_menu_text())
    st.divider()
    if st.button("🔄 Start New Order", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.app_stage = "chatting"
        st.session_state.bill = None
        st.session_state.order_items = []
        st.session_state.greeted = False
        st.rerun()

# Chat Display 
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🍕"):
        st.markdown(msg["content"])

# Bill Display
if st.session_state.app_stage == "bill" and st.session_state.bill:
    bill = st.session_state.bill
    with st.chat_message("assistant", avatar="🍕"):
        st.markdown("🧾 **Here's your bill:**")
        st.markdown(f"<div class='bill-box'>{format_bill(bill)}</div>", unsafe_allow_html=True)
        st.markdown(f"**Total payable: ₹{bill['total']}**")

        if st.button("💳 Proceed to Pay via UPI", use_container_width=True):
            st.session_state.app_stage = "payment"
            st.rerun()

# QR Payment Display 
if st.session_state.app_stage == "payment" and st.session_state.bill:
    total = st.session_state.bill["total"]
    with st.chat_message("assistant", avatar="🍕"):
        st.markdown(f"📲 **Scan the QR below to pay ₹{total} via UPI:**")

        qr_img = generate_upi_qr(amount=total)
        qr_bytes = qr_to_bytes(qr_img)
        st.image(qr_bytes, width=220, caption=f"Pay ₹{total} to demo@swayam")

        st.markdown("_After scanning, click the button below to confirm payment _")

        if st.button(" I've Paid! Confirm Order", use_container_width=True):
            st.session_state.app_stage = "confirmed"
            st.rerun()

#  Order Confirmed Display 
if st.session_state.app_stage == "confirmed":
    eta = random.randint(12, 20)
    with st.chat_message("assistant", avatar="🍕"):
        st.markdown(f"""
🎉 **Payment Confirmed! Your order is placed!**

<div class='status-badge'> Order #{random.randint(1000,9999)} Confirmed</div>

 **Estimated pickup time: {eta} minutes**

We'll call your token number at the counter. Grab a seat and relax!
        """, unsafe_allow_html=True)

        pizza_img_path = os.path.join(os.path.dirname(__file__), "assets", "pizza_ready.png")
        if os.path.exists(pizza_img_path):
            st.image(pizza_img_path, caption="Your fresh pizza is being made! ", width=300)

        st.success(f"Come collect your order in ~{eta} minutes. Enjoy your meal!")

#  Chat Input 
if st.session_state.app_stage == "chatting":
    user_input = st.chat_input("Type your order or ask anything... ")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.chat_message("user", avatar="🧑"):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar="🍕"):
            with st.spinner("Yummy Pizza is thinking... "):
                response = chat_with_agent(user_input, st.session_state.chat_history[:-1])

            if "ORDER_CONFIRMED" in response:
                clean_response = response.replace("ORDER_CONFIRMED", "").strip()
                if clean_response:
                    st.markdown(clean_response)

                st.session_state.order_items = [
                    {"name": "Margherita Pizza", "size": "Medium", "qty": 1, "price": 249},
                    {"name": "Garlic Bread", "size": "", "qty": 1, "price": 79},
                    {"name": "Coca Cola", "size": "", "qty": 1, "price": 49},
                ]
                st.session_state.bill = calculate_bill(st.session_state.order_items)
                st.session_state.app_stage = "bill"

                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": clean_response or "Great! Let me prepare your bill "
                })
                st.rerun()
            else:
                st.markdown(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})