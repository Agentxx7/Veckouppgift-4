def uppgift6_version1():
    todo_list = []

    print("** Todo list extravaganza **")

    while True:
        print("1. Se innehållet i din lista")
        print("2. Lägga till nya punkter i din lista")
        print("3. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            if len(todo_list) == 0:
                print("Din lista är tom")
            else:
                for item in todo_list:
                    print("+ " + item.capitalize())

        elif choice == "2":
            new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_item)
            print('Ok, lade till "' + new_item + '" i listan.')

        elif choice == "3":
            print("Avslutar todo-listan.")
            break

        else:
            print("Ogiltigt val, försök igen.")

        print(".")
        
def uppgift6_version2():
    todo_list = []

    print("** Todo list extravaganza **")

    while True:
        print("1. Se innehållet i din lista")
        print("2. Lägga till nya punkter i din lista")
        print("3. Markera som klar")
        print("4. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            if len(todo_list) == 0:
                print("Din lista är tom")
            else:
                for item in todo_list:
                    print("+ " + item.capitalize())

        elif choice == "2":
            new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_item)
            print('Ok, lade till "' + new_item + '" i listan.')

        elif choice == "3":
            done_item = input("Vilken grej är du färdig med? ")

            if done_item in todo_list:
                todo_list.remove(done_item)
                print('Ok, tog bort "' + done_item + '" från listan.')
            else:
                print("Den saken finns inte i listan.")

        elif choice == "4":
            print("Avslutar todo-listan.")
            break

        else:
            print("Ogiltigt val, försök igen.")

        print(".")

def uppgift6_version3():
    todo_list = []
    done_list = []

    print("** Todo list extravaganza **")

    while True:
        print("1. Se innehållet i din todo-lista")
        print("2. Lägga till nya punkter i din todo-lista")
        print("3. Markera som klar")
        print("4. Se färdiga saker")
        print("5. Lägg tillbaka färdig sak i todo-listan")
        print("6. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            if len(todo_list) == 0:
                print("Din todo-lista är tom")
            else:
                for item in todo_list:
                    print("+ " + item.capitalize())

        elif choice == "2":
            new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_item)
            print('Ok, lade till "' + new_item + '" i todo-listan.')

        elif choice == "3":
            done_item = input("Vilken grej är du färdig med? ")

            if done_item in todo_list:
                todo_list.remove(done_item)
                done_list.append(done_item)
                print('Ok, flyttade "' + done_item + '" till färdiga saker.')
            else:
                print("Den saken finns inte i todo-listan.")

        elif choice == "4":
            if len(done_list) == 0:
                print("Du har inte bockat av något ännu")
            else:
                for item in done_list:
                    print("- " + item.capitalize())

        elif choice == "5":
            item_to_restore = input("Vilken färdig sak vill du lägga tillbaka? ")

            if item_to_restore in done_list:
                done_list.remove(item_to_restore)
                todo_list.append(item_to_restore)
                print('Ok, lade tillbaka "' + item_to_restore + '" i todo-listan.')
            else:
                print("Den saken finns inte bland färdiga saker.")

        elif choice == "6":
            print("Avslutar todo-listan.")
            break

        else:
            print("Ogiltigt val, försök igen.")

        print(".")