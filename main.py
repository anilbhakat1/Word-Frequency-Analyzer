import re
from collections import Counter


def clean_text(text):
    """Remove extra whitespace and normalize spacing."""
    return " ".join(text.split())


def count_words(text):
    """Count case-insensitive words, ignoring punctuation."""
    cleaned_text = clean_text(text.lower())
    words = re.findall(r"\b[\w']+\b", cleaned_text)
    return Counter(words)


def main():
    print("=" * 55)
    print("           WORD FREQUENCY ANALYZER")
    print("=" * 55)
    print("Paste your paragraph below. Press Enter on an empty line to finish:\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    paragraph = " ".join(lines)

    if not paragraph.strip():
        print("\nNo text entered. Please run the program again.")
        return

    cleaned = clean_text(paragraph)
    frequencies = count_words(cleaned)

    print("\nCleaned paragraph:")
    print(cleaned)

    print("\nTotal words:", sum(frequencies.values()))
    print("Unique words:", len(frequencies))

    print("\nWord frequencies:")
    for word, count in frequencies.most_common():
        print(f"{word}: {count}")

    print("\nTop 3 most frequent words:")
    for rank, (word, count) in enumerate(frequencies.most_common(3), start=1):
        print(f"{rank}. {word} - {count} time(s)")


if __name__ == "__main__":
    main()
