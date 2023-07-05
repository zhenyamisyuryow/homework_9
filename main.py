contacts = {}


def input_error(func):
    def handler(*args):
        try:
            return func(*args)
        except KeyError:
            return "Error: key doesn't exist."
        except ValueError:
            return "Error: phone can only contain digits."
        except IndexError:
            return "Error: provide both name and phone number."
    return handler

@input_error
def hello(*args):
    return "Hi! How can I help you today?"

@input_error
def add(*args) -> None:
    phone = int(args[1])
    name = args[0]
    contacts[name] = phone
    return f"Success! {name} has been added to your contacts list."

@input_error
def change(name:str, phone:int):
    phone = int(phone)
    if name in contacts:
        contacts[name] = phone
        return f"Success! Phone number for {name} has been changed."
    else:
        return f"{name} was not found in contacts list."

@input_error
def phone(name: str):
    return contacts[name]

@input_error
def showall(*args):
    result = []
    for k,v in contacts.items():
        result.append(': '.join([k,str(v)]))
    return '\n'.join(result)
    
def main():

    func_maps = {
        "hello" : hello,
        "add" : add,
        "change" : change,
        "phone" : phone,
        "showall" : showall
    }

    print("Enter the first command:")
    
    while True:

        user_input = input(">>> ").lower()

        if user_input in ["good bye", "exit", "close"]:
            print("Good bye!")
            break

        input_parts = user_input.split()
        command = input_parts[0]
        args = input_parts[1:]

        if command in func_maps:
            print(func_maps[command](*args))
        else:
            print("Command is not supported. Please choose between: hello, add, change, phone or showall.")

if __name__ == "__main__":
    main()