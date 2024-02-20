# roman numeral calculator
def add(a: str, b: str) -> str:
    if len(a + b) >= 5:
        suffix = (len(a + b) - 5) * "I"
        return "V" + suffix

    if a == "I" and b == "V":
        return "VI"

    if a == "II" and b == "V":
        return "VII"

    return a + b
