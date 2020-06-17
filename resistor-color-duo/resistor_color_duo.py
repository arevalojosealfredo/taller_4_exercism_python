def value(colors):
    resistor_colors = {
        "Black" : 0,
        "Brown" : 1,
        "Red" : 2,
        "Orange" : 3,
        "Yellow" : 4,
        "Green" : 5,
        "Blue" : 6,
        "Violet" : 7,
        "Grey" : 8,
        "White" : 9
    }
    first_band = colors[0].capitalize()
    second_band = colors[1].capitalize()
    return (resistor_colors[first_band] *10 ) + resistor_colors[second_band]