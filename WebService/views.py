from django.http import HttpResponse
from Tile.pm import Pm

# View (in pm/views.py)
def pm_go(request, state="NOP"):
    """This method can be used to put the SUT into a specified PM state."""
    pm = Pm()
    pm.go()
    return HttpResponse("Going to %s" %state, mimetype="text/plain")

def pm_verify(request, state="NOP"):
    """This method can be used to verify the SUT is in a specified PM state."""
    pm = Pm()
    pm.verify()
    return HttpResponse("Verified in %s" %state, mimetype="text/plain")
