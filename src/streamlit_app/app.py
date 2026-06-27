import streamlit as st

st.set_page_config(page_title="Graph Foundation Model", layout="wide")

st.title("Graph Foundation Model")
st.write("Smoke-test Streamlit app.")

if st.button("Run health check"):
    st.success("app loaded")

