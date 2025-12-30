import os
from termcolor import colored

currentDirectory = r"D:/Workspace/Python/OnThiCumPython"
os.chdir(currentDirectory)


def main(filename: str, input: str, output: str):
    with open("test.inp", "w") as fTest:
        fTest.writelines(input)

    # Run script
    os.system(rf'python -u {currentDirectory}/{filename}')

    try:
        with open("test.out", "r") as f:
            out = ""
            for i in f.readlines():
                out = out + i
    except FileNotFoundError:
        print(colored(f"File output không tồn tại!", "red", "on_black"))
        exit()

    if out == output:
        print(colored("Succeeded!", "blue"))
    else:
        print(colored("failed.", "red"))
        print(f"The output was supposed to be: {colored(output, 'green')}")
        print(f"The actual output was: {colored(out, 'red')}")

    os.remove(f"{currentDirectory}/test.inp") ; os.remove(f"{currentDirectory}/test.out")


if __name__ == "__main__":
    input = "5\n1 2 3 4 4 3 2 2 4"
    output = "5"
    main("Bay15DaySo.py", input, output)  # Put filename in there
