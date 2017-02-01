# Import django modules
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# Import custom modules
from acerbi.waypoints.models import Waypoint
from acerbi import settings

def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    return render_to_response('waypoints/index.html', {
            'waypoints': waypoints,
            'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
            })
