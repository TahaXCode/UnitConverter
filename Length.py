def converter(entry, unit, unitconvert):
    entry = float(entry)

    # Dictionary mapping each unit pair to the conversion function
    conversion_map = {
        ("m", "km"): m_to_km,
        ("m", "mile"): m_to_mile,
        ("m", "cm"): m_to_cm,
        ("km", "m"): km_to_m,
        ("km", "mile"): km_to_mile,
        ("km", "cm"): km_to_cm,
        ("mile", "m"): mile_to_m,
        ("mile", "km"): mile_to_km,
        ("mile", "cm"): mile_to_cm,
        ("cm", "m"): cm_to_m,
        ("cm", "km"): cm_to_km,
        ("cm", "mile"): cm_to_mile,
    }

    # Look up the conversion function in the dictionary
    convert_function = conversion_map.get((unit, unitconvert))

    if convert_function:
        return convert_function(entry)
    else:
        return "Invalid unit or unit conversion!"


# Conversion functions for each pair of units
def m_to_km(value):
    return value / 1000


def m_to_mile(value):
    return value * 0.000621371


def m_to_cm(value):
    return value * 100


def km_to_m(value):
    return value * 1000


def km_to_mile(value):
    return value * 0.621371


def km_to_cm(value):
    return value * 100000


def mile_to_m(value):
    return value * 1609.34


def mile_to_km(value):
    return value * 1.60934


def mile_to_cm(value):
    return value * 160934


def cm_to_m(value):
    return value / 100


def cm_to_km(value):
    return value / 100000


def cm_to_mile(value):
    return value * 6.2137e-6
