def data_type(command):
    number = input()

    if command == "int":
        print(int(number) * 2)
    elif command == "real":
        print(f"{float(number) * 1.5:.2f}")
    elif command == "string":
        print(f"${number}$")


current_command = input()
data_type(current_command)
