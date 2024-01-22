# Anki Deck Generator

Generates an Anki deck given a JSON object that describes sentence cards used for language learning.

The goal for this project is to eventually have ChatGPT integration to generate an Anki deck of example sentences given a list of words you want to learn.

Sentence cards are effective for language learning because they help you learn vocabulary in the context of its actual usage, building intuition for grammar within a language.

## Example

Suppose you want to learn the following words in Croatian:

- Četkica za zube - Toothbrush
- Pasta za zube - Toothpaste
- Šampon - Shampoo

ChatGPT generates the following example sentences:

```json
{
    "flashcards": [
        {"Front": "Koristim četkicu za zube svaki dan.", "Back": "Četkica za zube - Toothbrush"},
        {"Front": "Stavio/la sam pastu za zube na četkicu.", "Back": "Pasta za zube - Toothpaste, staviti (to apply)"},
        {"Front": "Kupujem novi šampon za kosu.", "Back": "Šampon - Shampoo"}
    ]
}
```

The program then outputs a .apkg file for the Anki Deck in the given directory.


## Usage

1. **Install Dependencies:**

   Before running the script, make sure to install the necessary dependencies. You can do this using the following command:

   ```bash
   pip install genanki
   ```

 2. **Run Script**
    ```bash
        python3 card-generator.py --file <path to file> --deck-name <deckname>
    ```

## Contributing

I'd be surprised if anyone else will ever want to use this or contribute to this, but feel free to make a pull request if you want.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

