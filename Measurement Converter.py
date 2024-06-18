def measurement_converter():
    print("Select the conversion:")
    print("1. mm to cm")
    print("2. cm to m")
    print("3. m to km")
    print("4. inch to cm")
    print("5. ft to m")

    choice = int(input("Enter your choice (1-5): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} mm is {value / 10} cm")
    elif choice == 2:
        print(f"{value} cm is {value / 100} m")
    elif choice == 3:
        print(f"{value} m is {value / 1000} km")
    elif choice == 4:
        print(f"{value} inch is {value * 2.54} cm")
    elif choice == 5:
        print(f"{value} ft is {value * 0.3048} m")
    else:
        print("Invalid choice")


measurement_converter()
