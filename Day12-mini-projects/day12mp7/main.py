from textutils.count import word_count, char_count, unique_word_count
from textutils.sanitize import sanitize_basic
from textutils.analyze import most_common_word, word_frequency

def main():
    text = input("Enter some text: ")

    print("\n--- Sanitized Text ---")
    print(sanitize_basic(text))

    print("\n--- Counts ---")
    print(f"Characters: {char_count(text)}")
    print(f"Words: {word_count(text)}")
    print(f"Unique Words: {unique_word_count(text)}")

    print("\n--- Analysis ---")
    print(f"Most Common Word: {most_common_word(text)}")
    print(f"Word Frequencies: {word_frequency(text)}")

if __name__ == "__main__":
    main()
