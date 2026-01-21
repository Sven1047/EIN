import requests
from bs4 import BeautifulSoup
import urllib3

# This line suppresses the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_azlyrics(artist, song):
    # Format names: remove spaces and non-alphanumeric characters
    artist = "".join(filter(str.isalnum, artist.lower()))
    song = "".join(filter(str.isalnum, song.lower()))
    
    url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"
    
    # Using a User-Agent is highly recommended to avoid 403 Forbidden errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        # verify=False ignores SSL certificate errors
        response = requests.get(url, headers=headers, verify=False)
        
        if response.status_code != 200:
            return f"Error: Received status code {response.status_code}. Check artist/song spelling."

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # AZLyrics usually places the lyrics in the first div that has NO class and NO id
        # but is located inside the 'main-page' container.
        all_divs = soup.find_all("div", class_=None, id=None)
        for div in all_divs:
            text = div.get_text()
            if len(text) > 100:  # Lyrics are usually the longest text block without a class
                return text.strip()
        
        return "Lyrics div not found."

    except Exception as e:
        return f"Error: {e}"

# Execution
lyrics = scrape_azlyrics("Eminem", "Lose Yourself")
print(lyrics)
