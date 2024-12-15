def converter(entry, unit, unitconvert):
    entry = float(entry)

    # Dictionary mapping volume unit pairs to their conversion functions
    conversion_map = {
        ("L", "mL"): l_to_ml,
        ("L", "gal"): l_to_gal,
        ("mL", "L"): ml_to_l,
        ("mL", "gal"): ml_to_gal,
        ("gal", "L"): gal_to_l,
        ("gal", "mL"): gal_to_ml,
    }

    convert_function = conversion_map.get((unit, unitconvert))

    if convert_function:
        return convert_function(entry)
    else:
        return "Invalid unit or unit conversion!"


# Conversion functions
def l_to_ml(value):
    return value * 1000


def l_to_gal(value):
    return value * 0.264172


def ml_to_l(value):
    return value / 1000


def ml_to_gal(value):
    return value * 0.000264172


def gal_to_l(value):
    return value / 0.264172


def gal_to_ml(value):
    return value / 0.000264172
