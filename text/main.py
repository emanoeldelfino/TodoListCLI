#! python3
# Todo List CLI app with txt files.

import todo
import sys

if not todo.exists():
    todo.create()

while True:
    todo.content()

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
        todo.add(note)
    elif option == 2:
        while True:
            print('\nLine number')
            try:
                line = int(input(' > '))
                r = todo.remove(line)
                if not r:
                    raise ValueError
            except (ValueError, TypeError):
                print('Invalid line, try again.')
            except KeyboardInterrupt:
                sys.exit()
            else:
                break
    else:
        break

print('Thank you for preference. See you! :)')
