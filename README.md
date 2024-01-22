# anki-deck-generator

Generates an anki deck given a JSON object that describes sentence cards used for language-learning.

The goal for this project is to eventually have chat GPT integration to generate an anki deck of example sentences given
a list of words you want to learn.

Sentence cards are good for language learning because you learn vocabulary in context of its actual usage. It also helps build intuition for grammar within a language.

For example:

I want to learn the following words in Croatian:

Četkica za zube - Toothbrush
Pasta za zube - Toothpaste
Šampon - Kupujem novi šampon za kosu.

Chat GPT generates the following example sentences:

{
    "flashcards": [
        {"Front": "Koristim četkicu za zube svaki dan.", "Back": "Četkica za zube - Toothbrush"},
        {"Front": "Stavio/la sam pastu za zube na četkicu.", "Back": "Pasta za zube - Toothpaste, staviti (to apply)"},
        {"Front": "Kupujem novi šampon za kosu.", "Back": "Šampon - Shampoo"}
    ]
}

It then outputs a .apkg file for the anki deck.
