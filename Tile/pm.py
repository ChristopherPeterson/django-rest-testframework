from Tile.tile import Tile

class Pm(Tile):
    """
    Power Management Tile Class:
    """
    def __init__(self):
        """This method is Python's version of a Constructor/Initializer."""
        super(Pm, self).__init__() # Call Base Class Initializer first.
        self.async_methods = ['PBO']

    def get_version(self):
        return 0.3

    def go(self):
        """This method can be used to put a SUT into a specific state."""
        pass

    def verify(self):
        """This method can be used to verify a SUT is in a specific state."""
        pass