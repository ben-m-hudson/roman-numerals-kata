# roman numeral calculator
def add(a: str, b: str) -> str:
    if len(a + b) >= 5:
        suffix = (len(a + b) - 5) * "I"
        return "V" + suffix

    return a + b
