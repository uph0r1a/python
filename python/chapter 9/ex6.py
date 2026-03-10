with open("files/text1.txt") as f:
    words1 = set(f.read().lower().split())

with open("files/text2.txt") as f:
    words2 = set(f.read().lower().split())

print(
    f"The unique words contained in both files: {words1 | words2}\n"
    f"The words that appear in both files: {words1 & words2}\n"
    f"The words that appear in the first file but not the second: {words1 - words2}\n"
    f"The words that appear in the second file but not the first:{words2 - words1}\n"
    f"Words in either file but not both: {words1 ^ words2}"
)
