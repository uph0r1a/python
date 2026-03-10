print("Enter your name:", end="")
name = input()

print("Describe yourself:", end="")
description = input()

with open("files/personal.html", "w") as f:
    try:
        f.write(
            f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <center>
        <h1>{name}</h1>
    </center>
    <hr />
    {description}
    <hr />
</body>
</html>"""
        )
    except Exception as e:
        print(f"Error: {e}")
