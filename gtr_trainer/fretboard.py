NOTE_SEQUENCE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def get_note_at(tuning_note, fret):
    index = (NOTE_SEQUENCE.index(tuning_note) + fret) % 12
    return NOTE_SEQUENCE[index]

def get_interval_note(root_note, interval):
    interval_map = {
        'P1': 0, 'm2': 1, 'M2': 2, 'm3': 3, 'M3': 4,
        'P4': 5, 'd5': 6, 'P5': 7, 'm6': 8, 'M6': 9,
        'm7': 10, 'M7': 11, 'P8': 12
    }
    root_index = NOTE_SEQUENCE.index(root_note)
    return NOTE_SEQUENCE[(root_index + interval_map[interval]) % 12]