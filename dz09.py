def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return wrapper


def hello():
    return 'How can I help you?'


@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    contacts_book[name] = phone
    return f'Add {name}: {phone}'


@input_error
def change(*args):
    name = args[0]
    phone = args[1]
    if name in contacts_book:
        contacts_book[name] = phone
    return f'change {name}: {phone}'


@input_error
def phone(*args):
    name = args[0]
    if name in contacts_book:
        phone_number  = contacts_book[name]
    return f'phone: {phone_number}'


def show_all():
    return contacts_book


@input_error
def no_comand(*args):
    return 'Unknown command'


def parser(text: str) -> tuple[callable, tuple[str]]:
    if text.startswith('hello'):
        return hello, ()
    
    elif text.startswith('add'):
        return add, text.replace('add', '').strip().split()
    
    elif text.startswith('change'):
        return change, text.replace('change', '').strip().split()

    elif text.startswith('phone'):
        return phone, text.replace('phone', '').strip().split()
    
    elif text.startswith('show all'):
        return show_all, ()    
    
    return no_comand, ()


def main():
    global contacts_book
    contacts_book = dict()
    while True:
        user_input = input('>>>').lower()
        if user_input in ["good bye", "close", "exit"]:
            print('Good bye!')
            break
        command, data = parser(user_input)
        result = command(*data)
        print(result)


if __name__ == '__main__':
    main()