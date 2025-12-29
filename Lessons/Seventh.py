import streamlit as st
import pandas as pd
import time

st.title("Advanced Streamlit Components")

# st.data_editor: Editable dataframe
st.subheader("Data Editor")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Active": [True, False, True]
})
edited_df = st.data_editor(df)  # Returns edited dataframe
st.write("Edited data:", edited_df)

st.divider()

# st.select_slider: Slider with custom options
st.subheader("Select Slider")
size = st.select_slider("Pick size", options=["XS", "S", "M", "L", "XL"])
st.write(f"Selected: {size}")

color = st.select_slider("Pick color intensity", options=range(0, 101, 10), value=50)
st.write(f"Intensity: {color}%")

st.divider()

# st.toast: Temporary notification
st.subheader("Toast Notifications")
if st.button("Show Success Toast"):
    st.toast("Success!", icon="✅")
if st.button("Show Warning Toast"):
    st.toast("Warning message", icon="⚠️")
if st.button("Show Info Toast"):
    st.toast("Information", icon="ℹ️")

st.divider()

# st.form: Batch input submission
st.subheader("Form")
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Submitted: {name}, {age}")
        st.toast("Form submitted!", icon="✅")

st.divider()

# st.empty: Placeholder that can be replaced
st.subheader("Empty Placeholder")
placeholder = st.empty()  # Create placeholder
if st.button("Start Progress"):
    for i in range(5):
        placeholder.write(f"Progress: {i+1}/5")  # Update placeholder
        time.sleep(0.5)
    placeholder.success("Complete!")  # Replace with success message
