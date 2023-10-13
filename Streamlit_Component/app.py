import streamlit as st
from typing import Literal
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open("../../data/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)


def loginME():
    authenticator.login("Login", "main")


# def LogMeOut():
#     if st.session_state["authentication_status"]:
#         authenticator.logout("Logout", "main", key="121")
#         st.write(f'Welcome *{st.session_state["name"]}*')
#         st.title("Some content")
#     elif st.session_state["authentication_status"] is False:
#         st.error("Username/password is incorrect")
#     elif st.session_state["authentication_status"] is None:
#         st.warning("Please enter your username and password")


def ChangeMyPassword():
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(
                st.session_state["username"], "Reset password"
            ):
                st.success("Password modified successfully")
        except Exception as e:
            st.error(e)


def RegisterMe():
    try:
        if authenticator.register_user("Register user", preauthorization=False):
            st.success("User registered successfully")
    except Exception as e:
        st.error(e)


def ForgotPassword():
    try:
        (
            username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password,
        ) = authenticator.forgot_password("Forgot password")
        if username_of_forgotten_password:
            st.success("New password to be sent securely")
            # Random password should be transferred to user securely
        else:
            st.error("Username not found")
    except Exception as e:
        st.error(e)


b0 = st.button("Login me", on_click=loginME)
# st.button("Login me", on_click=LogMeOut)
b1 = st.button("Change Password", on_click=ChangeMyPassword)
b2 = st.button("Register Me", on_click=RegisterMe)
b3 = st.button("Forgot Password", on_click=ForgotPassword)
