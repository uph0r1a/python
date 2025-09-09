# Bài 5
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("So ban vua nhap la so chan")
    else:
        print("So ban vua nhap la so le")


def is_even(n):
    return n % 2 == 0


main()
