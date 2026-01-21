import csv
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def main():

    file_to_read = "ArianaGrande.csv"
    column_names, all_songtracks = read_csv_simple(file_to_read)

    # wir geben aus was für eine Struktur die Daten haben
    if all_songtracks is not None:
        print("Successfully read the file: ", file_to_read)
        print("Header/Column Names:", column_names)
        print("Total number of data rows read:", len(all_songtracks))
    
    # leere Zeile
    print("")
    
    # wir gehen jetzt durch alle Songs hindurch
    for i in range(len(all_songtracks)):
        print("Lied:", all_songtracks[i][1])
        print("Jahr:", all_songtracks[i][5])
        lyrics = all_songtracks[i][4] 
        
        sentiment = analyzer.polarity_scores(lyrics)
        print("Sentiment: ", sentiment['compound'])

        
def read_csv_simple(file_name):
    header = []
    data = []
    try:
        with open(file_name, mode='r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            try:
                header = next(csv_reader)
            except StopIteration:
                print(f"Warning: The file '{file_name}' is empty.")
                return [], []
            for row in csv_reader:
                data.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None
        
    return header, data

# call main
data = read_csv_simple("ArianaGrande.csv")
print(data)

