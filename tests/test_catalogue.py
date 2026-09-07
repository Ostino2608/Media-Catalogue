"""
Basic tests for catalogue.py.

Run with:
    pytest
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from catalogue import Movie, TVSeries, MediaCatalogue, MediaError  # noqa: E402


# --- Movie validation ---

def test_movie_creates_successfully_with_valid_data():
    movie = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    assert movie.title == 'The Matrix'
    assert movie.year == 1999
    assert movie.director == 'The Wachowskis'
    assert movie.duration == 136


def test_movie_rejects_empty_title():
    with pytest.raises(ValueError, match='Title cannot be empty'):
        Movie('   ', 1999, 'Someone', 100)


def test_movie_rejects_year_before_1895():
    with pytest.raises(ValueError, match='Year must be 1895 or later'):
        Movie('Old Film', 1800, 'Someone', 100)


def test_movie_rejects_empty_director():
    with pytest.raises(ValueError, match='Director cannot be empty'):
        Movie('A Movie', 2000, '  ', 100)


def test_movie_rejects_non_positive_duration():
    with pytest.raises(ValueError, match='Duration must be positive'):
        Movie('A Movie', 2000, 'Someone', 0)


def test_movie_str_format():
    movie = Movie('Inception', 2010, 'Christopher Nolan', 148)
    assert str(movie) == 'Inception (2010) - 148 min, Christopher Nolan'


# --- TVSeries validation (inherits Movie's rules) ---

def test_tv_series_creates_successfully_with_valid_data():
    series = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    assert series.seasons == 5
    assert series.total_episodes == 62
    # Inherited attributes from Movie:
    assert series.title == 'Breaking Bad'


def test_tv_series_rejects_invalid_seasons():
    with pytest.raises(ValueError, match='Seasons must be 1 or greater'):
        TVSeries('Show', 2020, 'Someone', 30, 0, 10)


def test_tv_series_rejects_invalid_total_episodes():
    with pytest.raises(ValueError, match='Total episodes must be 1 or greater'):
        TVSeries('Show', 2020, 'Someone', 30, 1, 0)


def test_tv_series_inherits_movie_validation():
    with pytest.raises(ValueError, match='Year must be 1895 or later'):
        TVSeries('Show', 1800, 'Someone', 30, 1, 10)


def test_tv_series_str_format():
    series = TVSeries('Stranger Things', 2016, 'The Duffer Brothers', 50, 4, 34)
    assert str(series) == (
        'Stranger Things (2016) - 4 seasons, 34 episodes, 50 min avg, '
        'The Duffer Brothers'
    )


# --- MediaCatalogue ---

def test_catalogue_starts_empty():
    catalogue = MediaCatalogue()
    assert str(catalogue) == 'Media Catalogue (empty)'
    assert catalogue.items == []


def test_catalogue_add_accepts_movie_and_tv_series():
    catalogue = MediaCatalogue()
    movie = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    series = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)

    catalogue.add(movie)
    catalogue.add(series)

    assert len(catalogue.items) == 2


def test_catalogue_add_rejects_non_movie_items():
    catalogue = MediaCatalogue()
    with pytest.raises(MediaError):
        catalogue.add('not a movie')


def test_media_error_carries_the_offending_object():
    catalogue = MediaCatalogue()
    try:
        catalogue.add(42)
    except MediaError as e:
        assert e.obj == 42
    else:
        pytest.fail('Expected MediaError to be raised')


def test_get_movies_excludes_tv_series():
    catalogue = MediaCatalogue()
    movie = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    series = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(movie)
    catalogue.add(series)

    movies = catalogue.get_movies()
    assert movies == [movie]


def test_get_tv_series_excludes_plain_movies():
    catalogue = MediaCatalogue()
    movie = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    series = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(movie)
    catalogue.add(series)

    tv_series = catalogue.get_tv_series()
    assert tv_series == [series]


def test_catalogue_str_groups_movies_and_series():
    catalogue = MediaCatalogue()
    catalogue.add(Movie('The Matrix', 1999, 'The Wachowskis', 136))
    catalogue.add(TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62))

    output = str(catalogue)
    assert 'Media Catalogue (2 items):' in output
    assert '=== MOVIES ===' in output
    assert '=== TV SERIES ===' in output
