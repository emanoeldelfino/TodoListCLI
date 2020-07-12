import sqlite3


def create():
    c = sqlite3.connect('todo.db').cursor()

    try:
        c.execute("SELECT rowid, * FROM notes")
    except sqlite3.OperationalError:
        c.execute("CREATE TABLE notes (note text)")
        print('DB criado com sucesso!')


def show():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM notes")

    items = c.fetchall()

    print('\n', 'Notes'.center(30, '-'))
    for id, item in items:
        print(' ', id, item + ';')
    print('', '-' * 30)

    conn.commit()

    conn.close()


def add(note):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO notes VALUES (?)", (note,))

    conn.commit()

    conn.close()


def delete(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("DELETE FROM notes WHERE rowid = (?)", id)

    conn.commit()

    conn.close()
