"""
Demo script: build a small catalogue of movies and TV series, and show
what happens when validation or type errors occur.

Usage:
    python example.py
"""

from catalogue import Movie, TVSeries, MediaCatalogue, MediaError

if __name__ == '__main__':
    catalogue = MediaCatalogue()

    try:
        movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
        catalogue.add(movie1)
        movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
        catalogue.add(movie2)
        series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
        catalogue.add(series1)
        series2 = TVSeries('Stranger Things', 2016, 'The Duffer Brothers', 50, 4, 34)
        catalogue.add(series2)
        print(catalogue)
    except ValueError as e:
        print(f'Validation Error: {e}')
    except MediaError as e:
        print(f'Media Error: {e}')
        print(f'Unable to add {e.obj}: {type(e.obj)}')

    print()
    print('--- Demonstrating error handling ---')

    # Trying to add something that isn't a Movie/TVSeries.
    try:
        catalogue.add('not a movie')
    except MediaError as e:
        print(f'Media Error: {e}')
        print(f'Unable to add {e.obj!r}: {type(e.obj)}')

    # Trying to create a Movie with invalid data.
    try:
        Movie('', 1999, 'Someone', 100)
    except ValueError as e:
        print(f'Validation Error: {e}')
