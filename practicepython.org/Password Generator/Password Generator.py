import random, string


def pw_gen(size, char=string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(char) for _ in range(size))


print(pw_gen(int(input("Enter password length: "))))
