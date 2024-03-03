import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    print(todo)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app. The subheader")
st.write("This is st write. We use it to write main things.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

the_input = st.text_input("Enter a todo", placeholder="Enter a todo",
                          on_change=add_todo, key='new_todo')

st.session_state
