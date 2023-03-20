import streamlit as st
from Functions import get_todos, write_todos
todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo in todos:
        st.write("You cant input todo that is already in todos")
    elif todo == "":
        st.write("Please write todo then press enter")
    else:
        todos.append(todo)
        write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="Enter todo", label_visibility="collapsed", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
