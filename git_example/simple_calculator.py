first_digit = input("Write first digit ")
second_digit = input("Write second digit ")
operation = input("Write operation(+-/*) ")


if operation == "+":
    print(f"Result: {int(first_digit) + int(second_digit)}")
elif operation == "-":
    print(f"Result: {int(first_digit) - int(second_digit)}")
elif operation == "*":
    print(f"Result: {int(first_digit) * int(second_digit)}")
elif operation == "/":
    try:
        print(f"Result: {int(first_digit) / int(second_digit)}")
    except ZeroDivisionError as e:
        print(f'Error: {e}')
else:
    print("Error: Unknown operation")