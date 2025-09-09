def arithmetic_arranger(problems, show_answers=False):
    # Step 1: Validate the input
    if len(problems) > 5:
        return "Error: Too many problems."

    # Lists to store each line of the formatted output
    first_line = []  # Stores the first operands (numbers on top)
    second_line = []  # Stores the operators and second operands (numbers on bottom)
    dashes = []  # Stores the separator lines (dashes)
    results = []  # Stores the results of the operations (if show_answers=True)

    for problem in problems:
        # Split each problem into components: first number, operator, and second number
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check for valid operators (only '+' and '-')
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if both operands are numeric
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if operands are within the allowed digit limit (max 4 digits)
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the required width for formatting (based on the longest operand)
        width = max(len(num1), len(num2)) + 2  # +2 accounts for operator and space

        # Format and store each component into respective lists
        first_line.append(num1.rjust(width))  # Right-align first operand
        second_line.append(
            operator + " " + num2.rjust(width - 2)
        )  # Right-align second operand with operator
        dashes.append("-" * width)  # Create a separator line with dashes

        # Calculate and store the result if show_answers is True
        if show_answers:
            result = str(eval(problem))  # Evaluate the arithmetic expression safely
            results.append(result.rjust(width))  # Right-align the result

    # Step 4: Arrange the output as a formatted string
    arranged_problems = (
        "    ".join(first_line)
        + "\n"  # Join first operands with 4 spaces between
        + "    ".join(second_line)
        + "\n"  # Join second operands with operators
        + "    ".join(dashes)  # Join separator lines
    )

    # If results are to be displayed, append them to the output
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


# Example usage to test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
