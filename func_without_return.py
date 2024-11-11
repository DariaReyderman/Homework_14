# a
def my_ascending(x: int, y: int):
    if x < y:
        print(x, y)
    else:
        print(y, x)


my_ascending(-12, 7)


# b
def my_details(word: str):
    print(word[0])
    print(word[len(word) // 2])
    print(word[-1])


my_details("AI is the best")


# c
def say_bool(x: bool):
    if x == True:
        print("Yes")
    else:
        print("No")


say_bool(True)
say_bool(False)


# d
def print_zugi(list1: list[int]):
    for i in list1:
        if i % 2 == 0:
            print("Even", end=" ")
        else:
            print("Odd", end=" ")


print_zugi([5, 3, 2, 10, 15, 14, 14])
print()


# e
def my_statistics(grades: list[int]):
    SENTINEL: int = -99
    while True:
        grade: int = int(input("Enter a grade: "))
        if grade == SENTINEL:
            break
        if grade < 0 or grade > 100:
            continue
        grades.append(grade)
    print(f"The maximum grade is {max(grades)}")
    print(f"The minimum grade is {min(grades)}")
    print(f"The count of grades is {len(grades)}")
    print(f"The average grade is {sum(grades) / len(grades)}")


my_statistics([])
