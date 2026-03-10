def main():
    word_index = {}

    input_file = "files/Kennedy.txt"
    output_file = "files/index.txt"

    with open(input_file) as file:
        line_number = 1

        for line in file:
            words = line.lower().split()

            for word in words:
                word = word.strip('.,!?;:"()')

                if word not in word_index:
                    word_index[word] = [line_number]
                else:
                    if line_number not in word_index[word]:
                        word_index[word].append(line_number)

            line_number += 1

    with open(output_file, "w") as file:
        for word in sorted(word_index):
            file.write(f"{word}: {word_index[word]}\n")

    print("Index file created successfully.")


main()
