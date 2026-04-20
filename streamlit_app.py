import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.title("Sales Dashboard")
name = st.text_input("User name")
st.write(f"Hello, {name}")

value = st.slider("Value", 0, 10, 5)
st.write("Current value:", value)


if "step" not in st.session_state:
    st.session_state.step = 1

st.write("Current step:", st.session_state.step)

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    submitted = st.form_submit_button("Submit")

def increment():
    st.session_state.count += 1

if "count" not in st.session_state:
    st.session_state.count = 0

st.button("Add", on_click=increment)
st.write(st.session_state.count)
