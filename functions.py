def get_todos(filepath="todo.txt"):
	with open(filepath, "r") as file_def:
		todos_def = file_def.readlines()
	return todos_def


#  THE FUNKTION GET AN ARGUMENT (AN INPUT)
def write_todos(todos_arg, filepath="todo.txt"):
	with open(filepath, "w") as file:
		file.writelines(todos_arg)


if __name__ == "__main__":
	print(__name__)