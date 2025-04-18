def test_get_note_at():
    from gtr_trainer.fretboard import get_note_at
    assert get_note_at('E', 1) == 'F'
    assert get_note_at('B', 1) == 'C'

def test_get_interval_note():
    from gtr_trainer.fretboard import get_interval_note
    assert get_interval_note('C', 'M3') == 'E'
    assert get_interval_note('F', 'P5') == 'C'