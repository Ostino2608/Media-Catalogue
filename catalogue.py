"""
Media Catalogue

A small object-oriented example modeling a catalogue of movies and TV
series. Demonstrates inheritance (TVSeries extends Movie), custom
exceptions, and simple validation.
"""


class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


class Movie:
    """Parent class representing a movie."""

    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')

        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')

        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return (
            f'{self.title} ({self.year}) - {self.seasons} seasons, '
            f'{self.total_episodes} episodes, {self.duration} min avg, {self.director}'
        )


class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []

    def add(self, media_item):
        """
        Add a Movie or TVSeries to the catalogue.

        Raises MediaError if `media_item` isn't a Movie (or subclass,
        like TVSeries).
        """
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def get_movies(self):
        """Return only the plain Movie items (excludes TVSeries)."""
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        """Return only the TVSeries items."""
        return [item for item in self.items if type(item) is TVSeries]

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'

        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'

        if series:
            result += '=== TV SERIES ===\n'
            for i, serie in enumerate(series, 1):
                result += f'{i}. {serie}\n'

        return result
