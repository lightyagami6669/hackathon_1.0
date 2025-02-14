import webbrowser

# Read coordinates from live_location.txt
with open('live_location.txt', 'r') as file:
    coordinates = file.read().strip()

# Construct the Google Maps URL
maps_url = f"https://www.google.com/maps?q={coordinates}"

# Open the URL in the default web browser
webbrowser.open(maps_url)