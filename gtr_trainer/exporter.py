import csv
from pathlib import Path

def export_anki_cards(cards, path="gtr_trainer/data/flashcards/anki_cards.csv"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for card in cards:
            writer.writerow(card)
    print(f"Exported {len(cards)} cards to {path}")