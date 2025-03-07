#!/usr/bin/env python3
import sys
from openpyxl import load_workbook

import tm


WS = "\t "
TMS_BLANK_SYM = "_"
DIR_TRANSLATION = {
        "<": tm.Dir.LEFT, "-": tm.Dir.HOLD, ">": tm.Dir.RIGHT,
        "L": tm.Dir.LEFT, "S": tm.Dir.HOLD, "R": tm.Dir.RIGHT,
        "←": tm.Dir.LEFT, "−": tm.Dir.HOLD, "→": tm.Dir.RIGHT,
        }


def parse_xlsx(path):
    wb = load_workbook(filename=path)
    sheet = wb.worksheets[0]
    values = list(sheet.values)
    symbols = values[0]

    delta = {}
    init_state = values[1][0]
    for state_line in values[1:]:
        state = state_line[0]
        for i, sym in enumerate(symbols[1:]):
            if sym is None:
                print(f"Found None value in symbols: {symbols}")
                continue
            elif not isinstance(sym, str):  # digits are interpreted as reals
                try:
                    sym = str(int(sym))
                except ValueError as e:
                    print(f"ValueError for sym: {sym} in symbols: {symbols} - {e}")
                    continue

            entry = state_line[i + 1]
            if not entry:
                entry = "N,_,-"

            if isinstance(entry, int):
                entry = str(entry)

            for ws in WS:
                entry = entry.replace(ws, "")

            nstate, nsym, d = entry.split(",")
            d = DIR_TRANSLATION[d]

            if sym == "_":
                sym = tm.BLANK_SYM

            if nsym == "_":
                nsym = tm.BLANK_SYM

            delta[(state, sym)] = (nstate, nsym, d)

    machine = tm.TuringMachine(init_state, delta)
    return machine

def main():
    pass


if __name__ == "__main__":
    main()
