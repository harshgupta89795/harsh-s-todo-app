import streamlit as st
from functions import get_todos,write_todos

todos = get_todos()
def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    write_todos(todos)


st.title("Harsh's App")
st.subheader("This is My Todo App")
st.write("This App is for Productivity")

for index, items in enumerate(todos):
    checkbox = st.checkbox(items, key=items)
    if checkbox: #to check the ticked checkbox
        todos.pop(index)# to remove checkbox item from the todos list
        write_todos(todos)#to write the new tod list after removing ticked item in the txt file
        del st.session_state[items]# to delete the item from website list
        st.experimental_rerun()# to rerun the program afer continously adding and removing todos

st.text_input(label='', placeholder="Add a new Todo..",
              key='new_todo', on_change=add_todo)
print("Hello")








