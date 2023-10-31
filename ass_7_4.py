integers = []
print(" Typing 'done' will exit the program ")
while True:
    user_input = input(" please enter an integer: ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        integers.append(number)
        average = sum(integers) / len(integers)
        print(f"{integers}, average = {average:.2f}")
    except ValueError:
        print(" please enter an integer.")
print("---------- Bye !! --------------")
