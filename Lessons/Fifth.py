import streamlit as st

st.title("Session State & Rerun Demo")

# st.session_state: Dictionary-like object that persists data across reruns
# Without it, variables reset to initial values on every interaction

# Initialize session state variables (runs only once per session)
if 'counter' not in st.session_state:  # Check if key exists
    st.session_state.counter = 0  # Store integer
if 'name' not in st.session_state:
    st.session_state.name = ""  # Store string
if 'todos' not in st.session_state:
    st.session_state.todos = []  # Store list

# Example 1: Counter - Shows state persistence
st.subheader("Counter with Session State")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.counter += 1  # Modify state
        st.rerun()  # Immediately rerun script to show updated value
with col2:
    if st.button("Decrement"):
        st.session_state.counter -= 1  # State persists between clicks
        st.rerun()  # Force refresh to display new count
with col3:
    if st.button("Reset"):
        st.session_state.counter = 0  # Reset state value
        st.rerun()  # Rerun to reflect reset
st.write(f"Count: {st.session_state.counter}")  # Always shows current state

# Example 2: Input persistence - State maintains user input
st.subheader("Persistent Input")
name_input = st.text_input("Enter name", value=st.session_state.name)  # Load from state
if name_input != st.session_state.name:  # Detect change
    st.session_state.name = name_input  # Update state
    st.rerun()  # Rerun to sync UI with state
if st.session_state.name:  # State persists across interactions
    st.write(f"Hello, {st.session_state.name}!")

# Example 3: Todo list - State stores complex data (lists)
st.subheader("Todo List")
new_todo = st.text_input("Add todo")
if st.button("Add") and new_todo:
    st.session_state.todos.append(new_todo)  # Modify list in state
    st.rerun()  # Rerun to display new todo immediately

# Loop through state list - persists across all interactions
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {todo}")
    if col2.button("Delete", key=f"del_{i}"):  # Unique key per button
        st.session_state.todos.pop(i)  # Remove from state
        st.rerun()  # Rerun to update list display
