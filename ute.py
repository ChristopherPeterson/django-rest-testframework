from Tile.tile import Tile

class Ute(object):
    """
    Unified Tile Executer (UTE):
    """
    test_tile       = Tile()
    keyword_class   = "pm"
    keyword_method1 = "go"
    keyword_method2 = "verify"
    input_states    = ["NOP", "g3", "ac", "reset",
                       "s3", "s4", "s5"]

    def __init__(self):
        """This method is Python's version of a Constructor/Initializer."""
        pass

    def execute(self):
        """This method iterates over the tile set and execute."""
        for state in self.input_states:
            print "================================"
            print "Request: " + self.keyword_class + ", " + self.keyword_method1 + ", " + state
            self.test_tile.send_rest_call(1000, self.keyword_class, self.keyword_method1, state)
            print "Response: " + self.test_tile.rest_response_html
            print "\nRequest: " + self.keyword_class + ", " + self.keyword_method2 + ", " + state
            self.test_tile.send_rest_call(1000, self.keyword_class, self.keyword_method2, state)
            print "Response: " + self.test_tile.rest_response_html + "\n"

    def test(self):
        """This method sends a test RESTful request to my Rails Web Service."""
        self.test_tile.send_test_rest_call(10000)
        print "\n\n\nRequest: cwpeter-desk:3000/resources/6:"
        print self.test_tile.rest_response_html

"""
This is the command line interface to this module.

If this file is called from the command prompt,
this code will be executed:
    "python <file_name>.py"

Also, to print the help for this file run the following
from the command line:
    "python <file_name>.py help
"""
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "help":
            print "HELP"
            print "    To run this script from the command line,"
            print "    type the following: \'python ute.py\'"
    else:
        ute_test = Ute()
        ute_test.execute()