def converter(entry, unit, unitconvert):
    entry = float(entry)

    # Dictionary mapping time unit pairs to their conversion functions
    conversion_map = {
        ("s", "min"): s_to_min,
        ("s", "h"): s_to_h,
        ("min", "s"): min_to_s,
        ("min", "h"): min_to_h,
        ("h", "s"): h_to_s,
        ("h", "min"): h_to_min,
    }

    convert_function = conversion_map.get((unit, unitconvert))

    if convert_function:
        return convert_function(entry)
    else:
        return "Invalid unit or unit conversion!"


# Conversion functions
def s_to_min(value):
    return value / 60


def s_to_h(value):
    return value / 3600


def min_to_s(value):
    return value * 60


def min_to_h(value):
    return value / 60


def h_to_s(value):
    return value * 3600


def h_to_min(value):
    return value * 60
