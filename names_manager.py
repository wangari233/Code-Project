FILENAME = "names.txt"
def load_names():
    try:
        with open(FILENAME, "r") as f:
            names = [line.strip() for line in f if line.strip()]
        return names
    except FileNotFoundError:
        return []

def save_names(names):
    with open(FILENAME, "w") as f:
        for name in names:
            f.write(name + "\n")

def main():
    names = load_names()

    if names:
        print("Previously saved names:")
        for index, name in enumerate(names, 1):
            print(f"{index}. {name}")
        print()
    else:
        print("No previously saved names found.\n")

    print("Enter names one per line. Type 'quit' or press Enter on an empty line to finish and save.")

    while True:
        name = input("Name: ").strip()
        if name.lower() in ("quit", "exit", ""):
            break
        names.append(name)
        print(f"Added: {name}")

    save_names(names)
    print(f"\nSaved {len(names)} name(s) to '{FILENAME}'.")
    print("Closing the application. Run the program again to see the saved names.")
    


if __name__ == "__main__":
    main()



