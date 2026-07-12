import requests
from ics import Calendar

def generate_master_almanac():
    # Replace with your exact GitHub username
    username = "jayyywake"
    
    # The raw URLs of your individual calendar files
    urls = [
        f"https://raw.githubusercontent.com/jayyywake/planetary-transits-calendar/refs/heads/main/planetary_transits.ics",
        f"https://raw.githubusercontent.com/jayyywake/biodynamic-zodiac-calendar/refs/heads/main/biodynamic_zodiac.ics",
        f"https://raw.githubusercontent.com/jayyywake/biodynamic-zodiac-calendar/refs/heads/main/biodynamic_zodiac.ics",
        f"https://raw.githubusercontent.com/jayyywake/wheel-of-the-year-calendar/refs/heads/main/wheel_of_the_year.ics",
        f"https://raw.githubusercontent.com/jayyywake/astrological-decans-calendar/refs/heads/main/astrological_decans.ics",
        f"https://raw.githubusercontent.com/jayyywake/astro-calendar/refs/heads/main/astrology.ics"
    ]

    master_cal = Calendar()

    for url in urls:
        try:
            # Fetch the raw .ics file from GitHub
            response = requests.get(url)
            response.raise_for_status()
            
            # Parse the calendar and merge its events
            cal = Calendar(response.text)
            for event in cal.events:
                master_cal.events.add(event)
                
            print(f"Successfully merged: {url.split('/')[4]}")
        except Exception as e:
            print(f"Failed to fetch or parse {url}: {e}")

    # Save the consolidated calendar
    with open("master_almanac.ics", "w") as f:
        f.writelines(master_cal.serialize_iter())

if __name__ == "__main__":
    generate_master_almanac()
