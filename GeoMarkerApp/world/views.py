import json
from django.shortcuts import get_object_or_404, render
from django.views import generic
from world.models import Letters
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.gis.geos import  Point
import psycopg2
import pdb


from django.core.serializers import serialize 

# Create your views here.
def index(request):
    data = str(serialize('geojson', Letters.objects.all(),
    geometry_field ='point', fields =('text',)))
    print(data)
    return render(request, 'world/index.html', {"data":data})



@csrf_exempt
def Letterpost(request):
    text = request.POST.get('text', None)
    lat = request.POST.get('lat', None)
    lon = request.POST.get('lon', None)
    print(text, lat, lon, type(lon), type(lat))
    pnt = Point( float(lon), float(lat), srid = 4326)
    letter = Letters(text=text,lat=lat,lon=lon, point=pnt)   
    letter.save()
    data={}
    data['response']= "Success!"
    return JsonResponse(data, content_type ='application/json', safe=False)






    #conn = psycopg2.connect("dbname='letterbox' user='postgres' host='127.0.0.1' password='*****!'")
    #cur =conn.cursor()
    #cur.execute("SELECT * FROM world_letters")
    #rows = cur.fetchall()
    #print(rows)

     