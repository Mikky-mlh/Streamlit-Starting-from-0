import streamlit as st

st.title("Containers, Expanders & Tabs Demo")

# Tabs: Organize content horizontally
tab1, tab2, tab3 = st.tabs(["Containers", "Expanders", "Combined"])

with tab1:
    st.header("Container Examples")
    
    # Container: Groups elements together
    with st.container():
        st.subheader("Container 1")
        st.write("Elements inside a container are grouped logically.")
        st.button("Button in Container 1")
    
    st.write("Content outside container")
    
    with st.container():
        st.subheader("Container 2")
        col1, col2 = st.columns(2)
        col1.metric("Metric 1", "100")
        col2.metric("Metric 2", "200")

with tab2:
    st.header("Expander Examples")
    
    # Expander: Collapsible section
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")
        st.code("print('Hello')")
    
    with st.expander("Another expander", expanded=True):
        st.write("This one starts expanded")
        st.slider("Slider", 0, 100)

with tab3:
    st.header("Combined Layout")
    
    with st.container():
        st.subheader("Container with Expanders")
        
        with st.expander("Section 1"):
            st.write("Nested expander in container")
            st.text_input("Input field")
        
        with st.expander("Section 2"):
            st.write("Another nested section")
            st.checkbox("Checkbox option")
