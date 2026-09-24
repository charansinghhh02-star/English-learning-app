import streamlit as st

st.set_page_config(page_title="Bike Puncture Finder")

st.title("🏍️ Bike Puncture Finder")

place = st.text_input("Enter Your City")

if st.button("Search"):

    if place.lower() == "rajahmundry":

        st.success("Found Nearby Workshops")

        st.write("🔧 Sai Bike Works")
        st.write("📞 9876543210")

        st.write("🔧 Durga Bike Repair")
        st.write("📞 9123456789")

        st.write("🔧 Maruthi Puncture Point")
        st.write("📞 9988776655")

    else:
        st.warning("No workshops found")

st.markdown("---")
st.write("Created by Charan Singh ❤️")