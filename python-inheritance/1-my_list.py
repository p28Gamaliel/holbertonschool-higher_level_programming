#!/usr/bin/python3
"""inherits from list."""


class MyList(list):
    """
    class List from inheritance.
    """

    def print_sorted(self):
        """
        prints the list in ascending sorted order.
        """
        print(sorted(self))
