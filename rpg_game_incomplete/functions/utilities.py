def menu(*items):
    for index, item in enumerate(items):
        print(f"{index + 1} - {item}")
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice > 0 and choice <= len(items):
                return choice
            else:
                print("Error! Type a valid number.")
            continue

        except ValueError:
            print("Type a number!")


def title(title, symbol="="):
    amount = len(title) + 10
    
    print(f"{symbol}" * amount)
    print(f"{title}".center(amount))
    print(f"{symbol}" * amount)