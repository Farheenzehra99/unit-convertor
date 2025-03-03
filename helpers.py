

def convert_units(value, unit_from, unit_to):
    print(f"Debug: Converting {value} from {unit_from} to {unit_to}")
    conversion_factors = {
        "km": {"miles": 0.621371, "meters": 1000},
        "miles": {"km": 1.60934, "meters": 1609.34},
        "meters": {"km": 0.001, "miles": 0.000621371},
        "feet": {"meters": 0.3048, "inches": 12},
        "inches": {"feet": 1/12, "cm": 2.54},
        "cm": {"inches": 1/2.54, "mm": 10},
        "mm": {"cm": 0.1},
        "kg": {"lbs": 2.20462, "grams": 1000},
        "lbs": {"kg": 0.453592, "grams": 453.592},
        "grams": {"kg": 0.001, "lbs": 0.00220462},
        "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9},
        "kelvin": {"celsius": lambda k: k - 273.15}
    }
    
    if unit_from in conversion_factors and unit_to in conversion_factors[unit_from]:
        factor = conversion_factors[unit_from][unit_to]
        return factor(value) if callable(factor) else value * factor
    else:
        return None

def get_conversion_fact(unit):
    facts = {
        "km": "1 km is equal to 0.621 miles.",
        "miles": "1 mile is equal to 1.609 km.",
        "meters": "1 meter is equal to 3.281 feet.",
        "feet": "1 foot is equal to 0.3048 meters.",
        "inches": "1 inch is equal to 2.54 cm.",
        "centimeters": "1 cm is equal to 0.3937 inches.",
        "millimeters": "1 mm is equal to 0.03937 inches.",
        "nanometers": "1 nanometer is equal to 1e-9 meters.",
        "yard": "1 yard is equal to 0.9144 meters.",

        "kg": "1 kg is equal to 2.204 lbs.",
        "lbs": "1 pound is equal to 0.4536 kg.",
        "grams": "1 gram is equal to 0.035 ounces.",
        "ounces": "1 ounce is equal to 28.35 grams.",
        "milligrams": "1 mg is equal to 0.001 grams.",
        "micrograms": "1 µg is equal to 1e-6 grams.",
        "tons": "1 ton is equal to 1000 kg.",

        "pascals": "1 Pascal is equal to 0.00001 bar.",
        "atm": "1 atmosphere is equal to 101.325 kPa.",
        "bar": "1 bar is equal to 100 kPa.",

        "mps": "1 meter per second is equal to 3.6 km/h.",
        "kph": "1 km/h is equal to 0.621 mph.",
        "mph": "1 mph is equal to 1.609 km/h.",
        "fps": "1 foot per second is equal to 0.3048 m/s.",

        "celsius": "0°C is equal to 32°F.",
        "fahrenheit": "32°F is equal to 0°C.",
        "kelvin": "0 Kelvin is -273.15°C.",

        "seconds": "1 second is equal to 1000 milliseconds.",
        "minutes": "1 minute is equal to 60 seconds.",
        "nanoseconds": "1 nanosecond is equal to 1e-9 seconds.",
        "microseconds": "1 microsecond is equal to 1e-6 seconds.",
        "hours": "1 hour is equal to 60 minutes.",
        "days": "1 day is equal to 24 hours.",
        "weeks": "1 week is equal to 7 days.",
        "months": "1 month is approximately 30.44 days.",
        "years": "1 year is equal to 365.25 days.",
        "century": "1 century is equal to 100 years.",

        "liters": "1 liter is equal to 1000 milliliters.",
        "milliliters": "1 milliliter is equal to 0.001 liters.",
        "gallons": "1 gallon is equal to 3.785 liters.",
        "cups": "1 cup is equal to 0.24 liters.",

        "joules": "1 joule is equal to 0.000239 kcal.",
        "watts": "1 watt is equal to 1 joule per second.",
        "watt-hours": "1 watt-hour is equal to 3600 joules.",
        "calories": "1 calorie is equal to 4.184 joules.",
        "kilowatt-hours": "1 kWh is equal to 3.6 million joules.",

        "bps": "1 bps (bit per second) is the basic unit of data transfer.",
        "kbps": "1 kbps is equal to 1000 bps.",
        "mbps": "1 mbps is equal to 1000 kbps.",
        "gbps": "1 gbps is equal to 1000 mbps.",
        "tbps": "1 tbps is equal to 1000 gbps.",

        "sq meters": "1 sq meter is equal to 10.764 sq feet.",
        "sq kilometers": "1 sq kilometer is equal to 247.1 acres.",
        "sq miles": "1 sq mile is equal to 2.59 sq kilometers.",
        "sq yards": "1 sq yard is equal to 0.836 sq meters.",
        "sq feet": "1 sq foot is equal to 0.0929 sq meters.",
        "hectares": "1 hectare is equal to 10,000 sq meters.",
        "acres": "1 acre is equal to 4046.86 sq meters.",
    }
    return facts.get(unit, "No fun fact available.")

