#! python3
# Todo List CLI app with SQLite database.

import db
import sys

db.create()

while True:
    db.show()

    print('''
 [1] Add a note;
 [2] Remove a note;
 [3] Exit.
    ''')

    while True:
        try:
            print('Option')
            option = int(input(' > '))
            if option not in range(1, 4):
                raise ValueError
        except (ValueError, TypeError):
            print('Invalid option, try again.')
        except KeyboardInterrupt:
            sys.exit()
        else:
            break

    if option == 1:
        note = input(' >> ')
        db.add(note)
    elif option == 2:
        while True:
            print('\nLine number')
            try:
                line = input(' > ')
                db.delete(line)
            except (ValueError, TypeError):
                print('Invalid line, try again.')
            except KeyboardInterrupt:
                sys.exit()
            else:
                break
    else:
        break

print('Thank you for preference. See you! :)')
