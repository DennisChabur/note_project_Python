import changes as ch


def show_menu():
    item = 1
    while item in range(1, 5):
        print(
            "\nВыберите пункт меню: \n1-создать заметку\n2-прочитать спискок заметок"
            "\n3-редактировать заметку\n4-удалить заметку"
            "\nДля выхода из меню нажмите любую клавишу")
        item = check_int_number()
        if item == 1:
            ch.add_notes()
        elif item == 2:
            ch.read_notes()
        elif item == 3:
            ch.correct_notes()
        elif item == 4:
            ch.dell_notes()


def check_int_number():
    text = input()
    if text.isdigit():
        return int(text)



show_menu()
