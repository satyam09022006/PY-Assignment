def calculate_notes(amount):
    denominations = [100, 50, 20, 10, 5, 2, 1]
    notes = {}

    for denomination in denominations:
        notes[denomination] = amount // denomination
        amount %= denomination

    return notes

def main():
    # Get user input
    amount = int(input("Enter the amount of money: "))

    # Calculate notes
    notes = calculate_notes(amount)

    # Print notes
    print("Number of notes required:")
    for denomination, count in notes.items():
        print(f"{denomination}: {count}")

if __name__ == "__main__":
    main()
