def converter(entry, unit, unitconvert):
    entry = float(entry)

    # Dictionary mapping each unit pair to the conversion function for weight units
    conversion_map = {
        ("kg", "g"): kg_to_g,
        ("kg", "lb"): kg_to_lb,
        ("kg", "oz"): kg_to_oz,
        ("g", "kg"): g_to_kg,
        ("g", "lb"): g_to_lb,
        ("g", "oz"): g_to_oz,
        ("lb", "kg"): lb_to_kg,
        ("lb", "g"): lb_to_g,
        ("lb", "oz"): lb_to_oz,
        ("oz", "kg"): oz_to_kg,
        ("oz", "g"): oz_to_g,
        ("oz", "lb"): oz_to_lb,
    }

    # Look up the conversion function in the dictionary
    convert_function = conversion_map.get((unit, unitconvert))

    if convert_function:
        return convert_function(entry)
    else:
        return "Invalid unit or unit conversion!"


# Conversion functions for each pair of units
def kg_to_g(value):
    return value * 1000


def kg_to_lb(value):
    return value * 2.20462


def kg_to_oz(value):
    return value * 35.274


def g_to_kg(value):
    return value / 1000


def g_to_lb(value):
    return value * 0.00220462


def g_to_oz(value):
    return value * 0.035274


def lb_to_kg(value):
    return value / 2.20462


def lb_to_g(value):
    return value / 0.00220462


def lb_to_oz(value):
    return value * 16


def oz_to_kg(value):
    return value / 35.274


def oz_to_g(value):
    return value / 0.035274


def oz_to_lb(value):
    return value / 16
