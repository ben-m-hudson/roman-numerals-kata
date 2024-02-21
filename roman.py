def add(a, b):
    simple_a = a.replace("IV", "IIII").replace("IX", "VIIII")
    simple_b = b.replace("IV", "IIII").replace("IX", "VIIII")

    simple_sum = simple_a + simple_b

    ordered_sum = "".join(reversed(sorted(simple_sum)))

    canonicalised_sum = (
        ordered_sum.replace("IIIII", "V")
        .replace("IIII", "IV")
        .replace("VV", "X")
        .replace("VIV", "IX")
    )

    return canonicalised_sum
