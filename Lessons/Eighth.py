import streamlit as st
import time

st.title("Spinner, Chat & Markdown")

# st.spinner: Loading indicator
st.subheader("Spinner")
if st.button("Load Data"):
    with st.spinner("Loading..."):  # Shows spinner during execution
        time.sleep(2)
    st.success("Data loaded!")

st.divider()

# st.chat_message: Chat interface
st.subheader("Chat Messages")
with st.chat_message("user"):  # User message bubble
    st.write("Hello, how are you?")

with st.chat_message("assistant"):  # Assistant message bubble
    st.write("I'm doing great! How can I help?")

with st.chat_message("user", avatar="🧑"):  # Custom avatar
    st.write("Can you explain Streamlit?")

st.divider()

# st.markdown: Formatted text
st.subheader("Markdown")
st.markdown("**Bold text** and *italic text*")  # Basic formatting
st.markdown("# Header 1\n## Header 2\n### Header 3")  # Headers
st.markdown("- Item 1\n- Item 2\n- Item 3")  # Lists
st.markdown("`code snippet`")  # Inline code
st.markdown("[Link to Streamlit](https://streamlit.io)")  # Links
st.markdown(":red[Red text] :blue[Blue text]")  # Colored text

st.divider()

# st.markdown with HTML: Render custom HTML
st.subheader("Markdown with HTML")
st.markdown("<h3 style='color: red;'>Red Header</h3>", unsafe_allow_html=True)
st.markdown("<p style='background-color: yellow; padding: 10px;'>Highlighted text</p>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><b>Centered bold text</b></div>", unsafe_allow_html=True)
