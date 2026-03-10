codes = {
    "A": "α",
    "a": "@",
    "B": "β",
    "b": "6",
    "C": "χ",
    "c": "<",
    "D": "δ",
    "d": "3",
    "E": "ε",
    "e": "2",
    "F": "φ",
    "f": "!",
    "G": "γ",
    "g": "9",
    "H": "η",
    "h": "^",
    "I": "ι",
    "i": "*",
    "J": "ψ",
    "j": ";",
    "K": "κ",
    "k": "-",
    "L": "λ",
    "l": ":",
    "M": "μ",
    "m": "`",
    "N": "ν",
    "n": "~",
    "O": "ω",
    "o": "_",
    "P": "π",
    "p": ".",
    "Q": "θ",
    "q": "?",
    "R": "ρ",
    "r": "]",
    "S": "σ",
    "s": "5",
    "T": "τ",
    "t": "+",
    "U": "υ",
    "u": "=",
    "V": "ζ",
    "v": "&",
    "W": "Ω",
    "w": "#",
    "X": "Ξ",
    "x": "-",
    "Y": "Υ",
    "y": "^",
    "Z": "Δ",
    "z": "7",
}

try:
    with open("files/text.txt") as f1:
        with open("files/encrypted.txt", "a") as f2:
            text = f1.read()
            for c in text:
                if c in codes:
                    f2.write(codes[c])
                else:
                    f2.write(c)
except Exception as e:
    print(f"Error: {e}")
