def prettyCity(city,country,population=""):
    if population:
        formatted = f"{city.strip().title()}, {country.strip().title()} - population {population}"
    else:
        formatted = f"{city.strip().title()}, {country.strip().title()}"
    return formatted