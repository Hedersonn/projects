def lines(text=None, size=50, format="-"):

    if not text:
        print(format * size)

    else:
        print(format * size)
        print(f"{text}".center(size))
        print(format * size)


def menu(*text, menu=True):
    amount = len(text)
    
    if menu:
        lines(text="Central")
    else:
        print("-" * 50)
    for numbering, txt in enumerate(text):
        print(f"{numbering + 1} - {txt}")
    lines()

    while True:

        try:
            choice = int(input("Your option > "))

            if 1 <= choice <= amount:
                return choice
            else:
                print("Invalid Option!")
        except:
            print("Error! Enter a valid value!")

        
def end_system():
    lines("Thank for testing")

    
