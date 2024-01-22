import genanki
import sys
import argparse
import json

def generate_anki_deck(cardJSON, deckName):

    model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
            'name': 'CardTemplate',
            'qfmt': '<div class="card">{{Front}}</div>',
            'afmt': '<div class="card">{{Front}}<hr id="answer"/>{{Back}}</div>',
            },
        ],
        css='''\
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
            '''
    )

    # Create a deck
    deck = genanki.Deck(
        2059400110,
        deckName
    )

    for flashcard in cardJSON:
        note = genanki.Note(
            model=model,
            fields=[flashcard['Front'], flashcard['Back']]
        )
        deck.add_note(note)

    package = genanki.Package(deck)

    package.write_to_file(f'{deckName}.apkg')

def parse_json(filePath):
    try: 
        with open(filePath, 'r') as file:
            data_array = json.load(file) 
            return data_array["flashcards"]
    
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' does not exist. Please try again with a new filepath.")
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}. Please ensure the file is in valid JSON and try again.")
        sys.exit(1)

    except KeyError as e:
        print(f"Error accessing key: {e}. Please ensure the JSON file is in the format as specified in README.md")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please yell at me.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", type=str, required=True,
                        help="path to json file that contains the flashcards json file.")
    parser.add_argument("--deck_name", type=str, required=True,
                        help="name of the deck to be outputted.")

    args = parser.parse_args()

    json_file_path = args.file
    deck_name = args.deck_name

    cardsJSON = parse_json(json_file_path)
    generate_anki_deck(cardsJSON, deck_name)

    print(f"Generated Anki Deck {deck_name}.apkg")

main()
