# 🎸 gtr-trainer

**gtr-trainer** is a command-line tool to help guitarists practice visualizing and locating musical intervals across the fretboard. It supports custom tunings (including Drop B), generates random interval challenges, and visualizes them in a familiar fretboard layout using ASCII art with Rich formatting.

---

## 🛠 Features

- Random root note and interval generation
- Interval visualization across all string and fret positions
- Drop B and standard tuning support
- Highlighted root (🟩) and interval (🟥) notes
- Export to Anki-compatible TSV format (optional)

---

## 🧰 Requirements

- Python 3.8+
- [rich](https://github.com/Textualize/rich)
- [click](https://click.palletsprojects.com/)

Install dependencies with:

```bash
pip install -e .
```

---

## 🚀 Usage

```bash
gtr-trainer [OPTIONS]
```

### Options

| Option            | Description                                              |
|-------------------|----------------------------------------------------------|
| `--tuning`        | Guitar tuning to use (`drop_b`, `standard`). Default: `drop_b` |
| `--range`         | Fret range (e.g. `0-12`). Default: `0-12`                |
| `--anki-output`   | Export the current challenge as an Anki flashcard        |

---

### 🔍 Example

```bash
gtr-trainer --tuning drop_b --range 0-12
```

**Output:**

```
--- Interval Practice ---
Tuning: drop_b
Root note: F# (string 4, fret 4)
Interval: M3 -> A#

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ String │ 0 │ 1 │ 2 │ ...                            ┃
┃    1   │ C# │ D │ D# │ ...                          ┃
┃    2   │ G# │ A │ A# │ ...  <- interval 🟥           ┃
┃    3   │ E │ F │ F# │ ...                           ┃
┃    4   │ B │ C │ C# │ ...  <- root 🟩               ┃
┃    5   │ F# │ G │ G# │ ...                          ┃
┃    6   │ B │ C │ C# │ ...                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 📦 Export to Anki

If you pass the `--anki-output` flag, a `.tsv` file will be saved to:

```
gtr_trainer/data/flashcards/anki_cards.csv
```

This file can be imported into [Anki](https://apps.ankiweb.net/) to help drill interval memory via spaced repetition.

---

## 🔧 Future Plans

- Interval quiz mode (without revealing answers)
- Reverse mode (guess root from interval)
- More tunings and modes (e.g., chords, scales)
- Web and desktop app versions

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 📬 Contact

Built by a digital nomad musician & programmer. Feel free to fork, tweak, or reach out for collaboration or freelance inquiries!
