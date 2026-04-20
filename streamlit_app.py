import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
value = st.slider("Value", 0, 10, 5)
st.write("Current value:", value)
