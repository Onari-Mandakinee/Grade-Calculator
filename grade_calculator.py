while True:
    name = input("Enter the student's name (or 'Exit' to quit): ")
    if name.lower() == "exit":
        break

    # Ask for 3 subject marks
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    # Calculate the average
    average = sum(marks) / 3

    # Determine grade
    if average >= 75:
        result = "A"
    elif average >= 60:
        result = "B"
    elif average >= 40:
        result = "C"
    else:
        result = "Fail"

    # Display the result
    print("-" * 30)
    print(f"Name   : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {result}")
    print("-" * 30)
    print()  # Blank line for separation