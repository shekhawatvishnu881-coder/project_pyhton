def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return " Error : can not divide by zero "
    return a/b
def power (a,b):
    return a**b
def modulus (a,b):
    if b==0:
        return " Error : can not divide by zero"
    return a%b

OPERATIONS={
    "1":("Add",add),
    "2":("Subtract",subtract),
    "3":("Multiply",multiply),
    "4":("Divide",divide),
    "5":("Power",power),
    "6":("Modulus",modulus),
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Simple Calculator ===")
    history = []

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print("  7. Show history")
        print("  0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "7":
            if not history:
                print("No calculations yet.")
            else:
                print("\n--- History ---")
                for item in history:
                    print(item)
            continue

        if choice not in OPERATIONS:
            print("Invalid choice. Try again.")
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        name, func = OPERATIONS[choice]
        result = func(a, b)
        print(f"Result: {result}")
        history.append(f"{name}: {a} and {b} = {result}")


if __name__ == "__main__":
    main()
        

