# Calculator GUI

A simple desktop calculator built with Python and [PySide6](https://doc.qt.io/qtforpython-6/) (Qt).

## Features

- Add, subtract, multiply and divide
- Brackets: one `()` button that opens a bracket, or closes one if a bracket is still open
- Decimal point
- `%` gives the remainder (modulo), e.g. `7 % 3 = 1`
- `del` removes the last character, `AC` clears everything
- Shows `error` for invalid sums such as dividing by zero

## Running it

You need Python 3 installed.

```bash
pip install -r requirements.txt
python test.py
```
