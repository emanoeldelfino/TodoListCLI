def exists():
    """
    Check if todo exists.
    """
    try:
        a = open('todo.txt', 'rt', encoding='utf-8')  # rt = read text
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True


def create():
    """
    Create todo text file to store the notes.
    """
    try:
        a = open('todo.txt', 'wt+', encoding='utf-8')  # wt+ = write text O + de 'wt' que cria o arquivo.
        a.close()
    except:
        print('Error when creating file')
    else:
        print(f'Todo created succesfuly!')


# def read_file():
def content():
    """
    Show the content of the todo text file formatted.
    """
    try:
        a = open('todo.txt', 'rt', encoding='utf-8')
    except:
        print('Error opening the file')
    else:
        num_line = 1
        print()
        for line in a:
            formt_line = (f'{num_line} * ' + line.strip('\n') + ';').strip('\r')
            print(formt_line)
            num_line += 1
        print()
    finally:
        a.close()


def add(line):
    """
    Add a new note to todo text file.
    :param add: Mandatory. Line that will be added in the end of todo text file.
    """
    try:
        a = open('todo.txt', 'at', encoding='utf-8')
    except:
        print('Error when opening todo text file.')
    else:
        try:
            a.write(line + '\n')
        except:
            print('Error when submiting line to todo.')
        else:
            print(f'New note added succesfuly!')
            a.close()


def remove(line_number):
    """
    Remove a note of todo.
    :param line_number: Number of line to be removed.
    :return: Line was removed?
    """
    try:
        with open('todo.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        print('Error when reading todo text file.')
    else:
        try:
            deleted = False
            line_n = 1
            with open('todo.txt', 'w', encoding='utf-8') as f:
                for num, line in enumerate(lines, 1):
                    if num != line_number:
                        f.write(line)
                    else:
                        deleted = True
                    line_n += 1

                if not deleted:
                    raise ValueError
        except Exception as err:
            print('Error when removing note.')
            print(err)
            return False
        else:
            print('Note removed succesfuly!')
            return True
