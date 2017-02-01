# Import django modules
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
# Import custom modules
from geodemo.waypoints.models import Waypoint
from geodemo import settings
from geodemo.waypoints.coordinates import *
import psycopg2

def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    return render_to_response('waypoints/index.html', {
            'waypoints': waypoints,
            'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
            })
			
			
def saveFromMatkain(request):
	'Hae matkain tietokannasta vanha data ja luo niista GIS yhteensopiva'
	dbhost = "localhost"
	dbuser = "matkain"
	dbpasswd = "mat08kain"
	dbname = "matkain"
	dbport = "5432"
	
	try:
		conn = psycopg2.connect("dbname="+dbname+" user="+dbuser+" host="+dbhost+" password="+dbpasswd)
	except:
		return HttpResponse("ERROR: DB Connection failed")
	
	cur = conn.cursor()
	
	try:
		cur.execute("""SELECT route_point_id, name, p, i from route_point where route_id='16' order by route_point_id""")
	except:
		return HttpResponse("ERROR: Query failed")
	
	rows = cur.fetchall()

	KKJ = {0: 'P', 1: 'I'}
	WGS84 = {0: 'La', 1: 'Lo'}

	for row in rows:
	    if len(row[1]) > 2:
			KKJ['P'] = row[2]
			KKJ['I'] = row[3]
			nimi = row[1]
			WGS84 = KKJxy_to_WGS84lalo(KKJ)
			# waypoint = Waypoint.objects.get(id=int(row[0]))
			# waypoint.geometry.set_x(float(WGS84['La']))
			Waypoint(name=nimi, geometry='POINT('+str(WGS84['Lo'])+' '+str(WGS84['La'])+')').save()
			# print "Nimi: %s Leveysaste: %f Korkeusaste: %f" % (nimi.encode("utf-8")$

	cur.close()
	return HttpResponse("Done")