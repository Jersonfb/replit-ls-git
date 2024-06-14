import streamlit as st

st.title("Github + streamlit")

query = st.text_input("¿Cual es tu consulta?")

st.markdown(f"Tu consulta es: {query}")
