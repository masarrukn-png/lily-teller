import streamlit as st
import random

st.title("🔮 Magic Fortune Teller 🔮")
st.write("I can see your future...")

name = st.text_input("What is your name, brave seeker?")

if name:
    st.write(f"Hello, **{name}** — the spirits know you well!")

    fortunes = [
        "Yes, definitely!",
        "No way!",
        "Ask again later...",
        "The stars say YES! ⭐",
        "Hmm, doesn't look good 😬",
        "Absolutely!",
        "Try again tomorrow",
        "It is certain!"
    ]

    question = st.text_input("Ask me a yes/no question:")

    if question:
        st.write(f"Hmm, you ask: *{question}*")
        if st.button("🔮 Consult the spirits!"):
            fortune = random.choice(fortunes)
            st.success(f"🔮 The spirits say: **{fortune}**")