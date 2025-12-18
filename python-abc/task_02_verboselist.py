#!/usr/bin/python3
"""Module for VerboseList class that extends list with notifications."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Add item to list and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print notification with count."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove item from list and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
