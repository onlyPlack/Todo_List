todo_a = {'id': 'a', 'title': 'learn python', 'completed': False}
todo_b = {'id': 'b', 'title': 'learn music', 'completed': False}
todo_c = {'id': 'c', 'title': 'learn math', 'completed': True}
todo_list = [todo_a, todo_b, todo_c]
while True:
    print('Welcome to To-Do List Application')

    print('a: view to-do list')
    print('b: add new to-do item')
    print('c: exit')
    choice = input('Enter your choice: ')
    if choice == 'a':
        print('To_do List: ')
        for item in todo_list:
            print(item['title'] + ' : ' + str(item['completed']))
    elif choice == 'b':

        valids_id = False
        while not valids_id:#check id unique
            new_id = input('Enter new id:')

            check_id = False
            for item_id in todo_list:
                if new_id == item_id['id']:                    
                    check_id = True                    
                    print('ID already exists. Please use a unique ID.')

                    break
            else:
                check_id = False
                break
        title_unique = False
        while not title_unique:#check title unique
            check_title = False
            new_do = input('Enter new task: ')
            for item_title in todo_list:

                if new_do == item_title['title']:

                    check_title = True
                    print('Task already exists. Please use a unique task.')
                    break
            else:
                check_title = False
                break
        while True:
            new_status = input('Enter new status: ')
            if new_status == 'True':

                new_status = True
                break
            elif new_status == 'False':
                new_status = False
                break
            else:
                print('Invalid status. Please enter True or False.')
            print('Status invalid, setting to False by default')
            new_status = False
            break
        new_do1 = {'id': new_id, 'title': new_do , 'completed': new_status}
        todo_list.append(new_do1)
        print('New to-do item added successfully')
        print('There are now', len(todo_list), 'items in the to-do list.')
    elif choice == 'c':
        print('Exit....')
        break

    else:
        print('Invalid choice. Please try again.')