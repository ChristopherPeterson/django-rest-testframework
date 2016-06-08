import abc
import urllib2

class ITile(object):
    """
    Tile Abstract Class:
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_version(self):
        """This method can be used to return the Tile's current version."""
        return NotImplemented

class Tile(ITile):
    """
    Tile Base Class:
    """
    async_methods = []
    rest_response = 0
    rest_response_html = ""

    def __init__(self):
        """This method is Python's version of a Constructor/Initializer."""
        pass
    
    def get_version(self):
        return 0.2

    def send_test_rest_call(self, num_bytes):
        """This method can be used to send a RESTful request to a distributed agent."""
        self.rest_response = urllib2.urlopen("http://localhost:8001/action")
        self.rest_response_html = self.rest_response.read(num_bytes)

    def send_rest_call(self, num_bytes, obj, method, state="NOP"):
        """This method can be used to send a RESTful request to a distributed agent."""
        self.rest_response = urllib2.urlopen("http://localhost:8000/"+obj+"/"+method+"/"+state)
        self.rest_response_html = self.rest_response.read(num_bytes)

