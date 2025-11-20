def calculate_notes(amount):
    denominations = [100, 50, 20, 10, 5, 2, 1]
    notes = {}

    for denomination in denominations:
        notes[denomination] = amount // denomination
        amount %= denomination

    return notes

def main():
   
    amount = int(input("Enter the amount of money: "))

   
    notes = calculate_notes(amount)

    print("Number of notes required:")
    for denomination, count in notes.items():
        print(f"{denomination}: {count}")

if __name__ == "__main__":
    main()