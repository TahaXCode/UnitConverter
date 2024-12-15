def converter(entry, unit, unitconvert):
    entry = float(entry)

    # Dictionary mapping temperature unit pairs to their conversion functions
    conversion_map = {
        ("C", "F"): c_to_f,
        ("C", "K"): c_to_k,
        ("F", "C"): f_to_c,
        ("F", "K"): f_to_k,
        ("K", "C"): k_to_c,
        ("K", "F"): k_to_f,
    }

    convert_function = conversion_map.get((unit, unitconvert))

    if convert_function:
        return convert_function(entry)
    else:
        return "Invalid unit or unit conversion!"


# Conversion functions
def c_to_f(value):
    return (value * 9 / 5) + 32


def c_to_k(value):
    return value + 273.15


def f_to_c(value):
    return (value - 32) * 5 / 9


def f_to_k(value):
    return (value - 32) * 5 / 9 + 273.15


def k_to_c(value):
    return value - 273.15


def k_to_f(value):
    return (value - 273.15) * 9 / 5 + 32
