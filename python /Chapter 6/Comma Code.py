def formatstr(ls):
    if not ls:
        return ""
    return ", ".join(ls[:-1]) + ", and " + ls[-1]


spam = ["apples", "bananas", "tofu", "cats"]
print(formatstr(spam))
