def convert_measurements(inches):
    
    inches_per_foot = 12
    inches_per_yard = 36
    inches_per_centimeter = 1 / 2.54
    inches_per_meter = 1 / 39.37

    # Calculate conversions
    feet = inches / inches_per_foot
    yards = inches / inches_per_yard
    centimeters = inches * (1 / inches_per_centimeter)
    meters = inches * (1 / inches_per_meter)

    print(f"{inches} inches is equal to:")
    print(f"  * Feet: {feet:.4f} ft")
    print(f"  * Yards: {yards:.4f} yd")
    print(f"  * Centimeters: {centimeters:.4f} cm")
    print(f"  * Meters: {meters:.4f} m")

def main():
    # Get user input
    inches = float(input("Enter a measurement in inches: "))

    # Convert and print measurements
    convert_measurements(inches)

if __name__ == "__main__":
    main()