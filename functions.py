Filepath = "t.txt"
def get_todos(filepath=Filepath): # custom functions
    """Read a text file and a return a list of to-dos"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
print(help(get_todos))

def write_todos(todos_arg, filepath="t.txt"): #syntax is different
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())



