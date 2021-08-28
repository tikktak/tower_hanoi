number = int(input("Enter the number of disks: "))

def tower_hanoi(number, a, b, c):
    if number == 1:
        print(a+c)
    else:
        tower_hanoi(number-1, a, c, b)
        print(a+c)
        tower_hanoi(number-1, b, a, c)

tower_hanoi(number, "A", "B", "C")
