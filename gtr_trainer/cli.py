import click
import random
from .tunings import tunings
from .fretboard import get_note_at, get_interval_note
from .visualizer import render_fretboard
from .exporter import export_anki_cards

@click.command()
@click.option('--tuning', default='drop_b', help='Tuning name')
@click.option('--range', 'fret_range', default='0-12', help='Fret range, e.g. 0-12')
@click.option('--anki-output', is_flag=True, help='Export questions as Anki cards')
def main(tuning, fret_range, anki_output):
    tuning_notes = tunings.get(tuning)
    if not tuning_notes:
        print(f"Tuning '{tuning}' not found.")
        return

    low, high = map(int, fret_range.split('-'))
    interval_list = ['m2', 'M2', 'm3', 'M3', 'P4', 'P5', 'm6', 'M6', 'm7', 'M7', 'P8']
    cards = []

    root_string = random.randint(1, 6)
    root_fret = random.randint(low, high)
    root_note = get_note_at(tuning_notes[6 - root_string], root_fret)
    interval = random.choice(interval_list)
    interval_note = get_interval_note(root_note, interval)

    root_fret_map = {(root_string, root_fret)}
    interval_fret_map = set()
    for s in range(1, 7):
        for f in range(low, high + 1):
            note = get_note_at(tuning_notes[6 - s], f)
            if note == interval_note:
                interval_fret_map.add((s, f))

    print("\n--- Interval Practice ---")
    print(f"Tuning: {tuning}")
    print(f"Root note: {root_note} (string {root_string}, fret {root_fret})")
    print(f"Interval: {interval} -> {interval_note}\n")

    render_fretboard(tuning_notes, root_fret_map, interval_fret_map, range(low, high + 1))

    if anki_output:
        question = f"Where is the {interval} of {root_note} on string {root_string} at fret {root_fret}?"
        answer = interval_note
        cards.append((question, answer))
        export_anki_cards(cards)
