# Word Frequency Analyzer (Python)

A beginner-friendly Python project that accepts a paragraph from the user, cleans extra whitespace, counts each unique word using a dictionary-like frequency counter, and displays the three most frequent words.

## Features

- Accepts a multi-line paragraph from the user.
- Removes extra spaces, tabs, and line breaks.
- Treats uppercase and lowercase versions of a word as the same word.
- Ignores punctuation while counting words.
- Displays total words and unique words.
- Shows the frequency of every word and the top three most frequent words.
- Uses only Python's standard library.

## Requirements

- Python 3.8 or newer
- No external packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

4. Paste or type your paragraph.
5. Press Enter on an empty line to finish input.

## Example

**Input:**

```text
Python is easy to learn. Python is powerful.
```

**Sample output (main results):**

```text
Total words: 8
Unique words: 6

Word frequencies:
python: 2
is: 2
easy: 1
to: 1
learn: 1
powerful: 1

Top 3 most frequent words:
1. python - 2 time(s)
2. is - 2 time(s)
3. easy - 1 time(s)
```

Note: If words are tied, Python keeps their order of first appearance in the paragraph.

## Concepts used

- Variables and strings
- Functions
- Loops and conditional statements
- Lists
- Regular expressions (`re`)
- Dictionary-based word counting (`collections.Counter`)

## Project structure

```text
word_frequency_project/
├── main.py
├── README.md
└── .gitignore
```

## Author

Anil Bhakat 
