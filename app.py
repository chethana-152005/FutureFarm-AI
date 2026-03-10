import streamlit as st
from llm import ask_llm
from translator import translate_text
from crop_data import get_crop_info
from schemes import get_schemes
from auth import signup, login


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="FutureFarmAI - AI Agriculture Assistant",
    page_icon="🌾",
    layout="wide"
)


# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN / SIGNUP ----------------

if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Sign Up"]
    )

    if menu == "Login":

        st.title("🔐 Farmer Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login(username, password):

                st.session_state.logged_in = True

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Invalid credentials")


    if menu == "Sign Up":

        st.title("📝 Create Account")

        new_user = st.text_input("Username")

        new_pass = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Sign Up"):

            if signup(new_user, new_pass):

                st.success("Account created successfully")

            else:

                st.error("User already exists")


# ---------------- MAIN DASHBOARD ----------------

else:

    st.title("🌾 AI Powered Agriculture Assistant")


    # ---------- LANGUAGE ----------

    language = st.selectbox(
        "Select Language",
        ["English", "Hindi", "Telugu", "Tamil", "Marathi", "Kannada"]
    )


    # ---------- AI QUERY ----------

    st.header(
        translate_text("Ask Farming Question", language)
    )

    query = st.text_input(
        translate_text(
            "Type your farming question here",
            language
        )
    )

    if st.button(
        translate_text("Ask AI", language)
    ):

        if query:

            response = ask_llm(query, language)

            translated = translate_text(
                response,
                language
            )

            st.success(translated)


    # ---------- CROP INFORMATION ----------

    st.header(
        translate_text("Crop Information", language)
    )

    crop = st.text_input(
        translate_text(
            "Enter Crop Name (Example: Rice)",
            language
        )
    )

    if st.button(
        translate_text("Get Crop Details", language)
    ):

        if crop:

            data = get_crop_info(crop)

            if data:

                st.subheader(
                    translate_text("Crop Details", language)
                )

                st.write(
                    translate_text("Growing Time:", language),
                    data["growing_time"]
                )

                st.write(
                    translate_text("Season:", language),
                    data["season"]
                )

                st.write(
                    translate_text("Seeds:", language),
                    ", ".join(data["seeds"])
                )

                st.write(
                    translate_text("Fertilizers:", language),
                    ", ".join(data["fertilizers"])
                )

                st.write(
                    translate_text("Pesticides:", language),
                    ", ".join(data["pesticides"])
                )

            else:

                st.error(
                    translate_text(
                        "Crop not found in database",
                        language
                    )
                )


    # ---------- GOVERNMENT SCHEMES ----------

    st.header(
        translate_text(
            "Government Schemes for Farmers",
            language
        )
    )

    if st.button(
        translate_text("Show Schemes", language)
    ):

        schemes = get_schemes()

        for name, info in schemes.items():

            st.subheader(
                translate_text(name, language)
            )

            st.write(
                translate_text(info, language)
            )


    # ---------- LOGOUT ----------

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()


# ---------- FOOTER ----------

st.markdown("---")

st.caption(
    "🌾 AI Agriculture Assistant - Helping farmers with crop knowledge, fertilizers, seeds, and government schemes"
)
