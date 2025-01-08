#!/usr/bin/env python3

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./aniweather.py <city>")
    sys.exit(1)

arg = sys.argv[1]

def get_weather(city_name):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    geocoding_response = requests.get(geocoding_url)

    if geocoding_response.status_code == 200:
        geocoding_data = geocoding_response.json()
        if geocoding_data['results']:
            latitude = geocoding_data['results'][0]['latitude']
            longitude = geocoding_data['results'][0]['longitude']

            # Now get the weather data using latitude and longitude
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            weather_response = requests.get(weather_url)

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                current_weather = weather_data['current_weather']
                temperature = current_weather['temperature']
                return temperature

            else:
                print("Failed")
        else:
            print("City not found.")
    else:
        print("Failed")

city_name = arg
weather_data = get_weather(city_name)

if weather_data > 30:
    reaction = "SO HOT!"
elif weather_data > 20:
    reaction = "It's warm, like your smile."
elif weather_data > 10:
    reaction = "It's a bit chilly!"
else:
    reaction = "Brr! It's cold!"

# Function to center text within a given width
def center_text(text, width):
    return f"* {text.center(width - 1)} *"  # Subtract 4 for the stars and spaces

# Create the balloon with centered text
balloon = [
    "            **********            ",
    "        **              **        ",
    "     **                    **     ",
    "   **                        **   ",
    "  *                            *  ",
    " *                              * ",
    center_text("Sensei!", 30),
    center_text("Current temperature", 30),
    center_text(f"in {city_name}: {weather_data}°C", 30),
    center_text(f"{reaction}", 30),
    " *                              * ",
    " *                              * ",
    "  *                            *  ",
    "   **                        **   ",
    "     **                    **     ",
    "        **              **        ",
    "            **********            "
]

# ASCII art
ascii_art = """


⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⡠⢴⣴⣾⣿⡿⠓⡠⠀⠀⠀⠀⠠⢄⠁⢀⠀⠀
⠀⠀⠀⠀⠀⠳⣽⡽⠀⠀⡠⢊⣴⣿⣿⣿⣡⠖⠁⣀⡤⢖⠟⠁⡠⠀⡙⢿⣷⣄
⠀⠀⠐⡀⠀⠀⠀⠀⢠⣾⣿⣿⢽⣿⣿⣿⣥⠖⣻⣯⡾⠃⠀⡔⡀⠀⣷⢸⢿⣿
⠀⠀⠀⢰⠀⠀⠀⢠⢟⣿⠃⢀⣾⣿⠟⠋⢀⡾⢋⣾⠃⣠⡾⢰⡇⡇⣿⣿⡞⣿
⠀⠀⡤⣈⡀⠀⢀⠏⣼⣧⡴⣼⠟⠁⠀⠀⡾⠁⣾⡇⣰⢿⠃⢾⣿⣷⣿⣿⣇⢿
⠀⠀⠱⠼⠊⠀⠄⡜⣿⣿⡿⠃⠈⠁⠀⢸⠁⢠⡿⣰⢯⠃⠀⠘⣿⣿⣿⣿⣿⠸
⠀⠀⠀⠀⠀⠀⡘⡀⣸⣿⣱⡤⢴⣄⠀⠈⠀⠘⣷⠏⠌⠢⡀⠀⢿⣿⣿⣿⡟⡄
⠀⠀⠀⠀⢀⣌⠌⣴⣿⣿⠃⣴⣿⣟⡇⠀⠀⠀⠟⠀⠀⠀⠈⠢⢈⣿⡟⣿⡗⡇
⠀⠀⢀⡴⡻⣡⣾⠟⢹⡇⠀⡇⢄⢿⠇⠀⠀⠀⠀⠀⠀⣽⣶⣄⡀⠘⢷⡹⣿⣿
⠀⠀⣧⣾⡿⠋⠁⢀⡜⠙⡄⠓⠐⠁⠀⠀⠀⠀⠀⠀⡼⠛⠻⣟⠛⣆⠈⢷⣿⣿
⣴⣾⣟⣵⣿⣿⣿⣁⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⠠⠔⡹⠀⢸⠀⣼⣿⣿
⠿⡽⢫⡉⠀⣠⠔⠁⡀⠕⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠖⠊⠀⠀⢊⣾⢿⡿⠉
⠀⠁⠀⡹⢨⠁⠐⠈⢀⡠⠐⠁⠄⠡⡀⡀⠀⠀⠀⠀⠀⠀⠀⠠⠶⢛⡨⠊⠀⠀
⠀⠀⡜⠀⠈⣂⠀⠀⠀⠀⡠⠐⠉⡆⠀⣀⢀⣀⣀⣀⡀⠀⠀⣀⠴⣁⡀⠤⠀⠀
⠀⠈⠀⠀⠀⡇⠑⢄⠀⠀⠀⠀⣲⢥⡎⠀⢰⠀⢸⠀⢀⠉⠙⣿⣧⣀⣀⣂⣤⣼
⠀⠀⠀⠆⠁⠃⠀⠀⠈⠒⠒⠊⣸⠚⠁⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠈⠚
⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⢀⠋⢆⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠂⠀⠀⠐⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

print("\n")

def print_side_by_side(balloon, ascii_art):
    ascii_lines = ascii_art.strip().split('\n')
    
    max_lines = max(len(balloon), len(ascii_lines))
    balloon += [' ' * len(balloon[0])] * (max_lines - len(balloon))
    ascii_lines += [' ' * len(ascii_lines[0])] * (max_lines - len(ascii_lines))
    
    for b_line, a_line in zip(balloon, ascii_lines):
        print(b_line + '   ' + a_line)

print_side_by_side(balloon, ascii_art)

