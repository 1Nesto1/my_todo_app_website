FILEPATH = "todos.txt"

def get_todos(pathfile=FILEPATH):
    """ Read a text file and return the list of
        to-do items."""                         # można dzięki funkcji help(get_todos) wyświetlić tę wiadomość
    with open(pathfile, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, pathfile=FILEPATH):
    """ Writes a to-do item list in the text file."""
    with open(pathfile, 'w') as file:
        file.writelines(todos_arg)


print(__name__)   # to jest normalnie czytane jako str "main" w tym kodzie ale jeśli to importujemy gdzie indziej
                  # to wtedy ta variable będzie mieć str z nazwą tego pliku tutaj czyli "functions"
if __name__ == "__main__":
    print(get_todos())