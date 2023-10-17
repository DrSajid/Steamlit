import streamlit as st


from decouple import config

PASSWORD = config("PASSWORD")



if "password" not in st.session_state:
    st.session_state.password = ""


def use_component():
    st.balloons()
    st.header("Congradulation you have been successfully logged in!")


if st.session_state.password == PASSWORD:
    use_component()
elif st.session_state.password != PASSWORD:
    password_holder = st.empty()
    password = password_holder.text_input("Please enter your password", type="password")
    st.session_state.password = password
    if password and st.session_state.password == PASSWORD:
        password_holder.empty()
        st.success("Logged in Successfully")
        use_component()
    elif password and st.session_state.password != PASSWORD:
        st.error("Wrong password")
