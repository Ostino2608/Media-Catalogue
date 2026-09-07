# Media Catalogue

A small object-oriented Python project that models a catalogue of movies
and TV series. It demonstrates class inheritance, input validation, and
custom exception handling.

## Features

- `Movie` class with validation (title, year, director, duration)
- `TVSeries` class that extends `Movie` with seasons and episode counts
- `MediaCatalogue` container that stores mixed media types
- Separate lookups for plain movies vs. TV series
- A custom `MediaError` exception carrying the invalid object that
  triggered it, for clear error handling

## Project structure

```
media-catalogue/
├── catalogue.py             # Movie, TVSeries, MediaCatalogue, MediaError
├── example.py                 # Demo script
├── tests/
│   └── test_catalogue.py      # Test suite (pytest)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

```bash
git clone https://github.com/<your-username>/media-catalogue.git
cd media-catalogue
pip install -r requirements.txt   # only needed to run the tests
```

No external libraries are required to run the project itself — it only
uses Python's standard library.

## Usage

```python
from catalogue import Movie, TVSeries, MediaCatalogue, MediaError

catalogue = MediaCatalogue()

catalogue.add(Movie('The Matrix', 1999, 'The Wachowskis', 136))
catalogue.add(TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62))

print(catalogue)
```

Output:

```
Media Catalogue (2 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
=== TV SERIES ===
1. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

### Handling invalid input

```python
try:
    catalogue.add('not a movie')
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj!r}: {type(e.obj)}')
```

```
Media Error: Only Movie or TVSeries instances can be added
Unable to add 'not a movie': <class 'str'>
```

Or run the included demo, which walks through both the happy path and
error handling:

```bash
python example.py
```

## Running the tests

```bash
pytest
```

18 tests cover validation rules for `Movie` and `TVSeries`, inheritance
behavior, catalogue membership, and the `MediaError` exception.

## Known limitations / next steps

This is a learning project, so it's intentionally simple. Ideas for
extending it:

- `title`/`director` validation assumes a string is passed in — passing
  a non-string (like a number) will raise an `AttributeError` rather
  than a friendly `ValueError`. Worth adding an explicit type check.
- Add a `Documentary` or `Anime` subclass to show more inheritance depth.
- Support removing items from the catalogue, and searching by title/year.
- Persist the catalogue to a file (JSON) instead of losing it on exit.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE)
for details.
