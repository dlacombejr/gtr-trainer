from rich.console import Console
from rich.table import Table
from .fretboard import get_note_at

def render_fretboard(tuning, root_fret_map, interval_fret_map, fret_range=range(0, 13)):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("String")
    for fret in fret_range:
        table.add_column(str(fret))

    # String 1 is the highest pitch (rightmost in tuning), should be top row
    for i in range(6):
        string_num = 1 + i
        string_note = tuning[-(i + 1)]
        row = [f"{string_num}"]
        for fret in fret_range:
            symbol = get_note_at(string_note, fret)
            if (string_num, fret) in root_fret_map:
                row.append(f"[bold green]{symbol}[/]")
            elif (string_num, fret) in interval_fret_map:
                row.append(f"[bold red]{symbol}[/]")
            else:
                row.append(symbol)
        table.add_row(*row)

    console.print(table)
