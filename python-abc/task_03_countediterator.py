#!/usr/bin/python3
"""Module for CountedIterator class that tracks iteration count."""


class CountedIterator:
    """An iterator wrapper that counts items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as iterator."""
        return self

    def __next__(self):
        """Fetch next item, increment counter, raise StopIteration if done."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count
