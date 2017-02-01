# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from rdflib.Graph import Graph
from rdflib.Literal import Literal
from rdflib.Namespace import Namespace
#from django.http import HttpResponse

def kommuner(request):

    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/municipality/municipality.rdf") # Kommun

    graph_as_list = []
    c3_85_list = [] # u'Å'
    c3_84_list = [] # u'Ä'
    c3_96_list = [] # u'Ö'
    
    """ ---------- LÄN ---------- """
    def get_county_list():

        g_county = Graph()
        g_county.parse("http://kulturarvsdata.se/resurser/aukt/geo/county/county.rdf") # Landskap
        county_list = []
        
        for row in g_county.query("\
            BASE <http://kulturarvsdata.se/>\
            PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
            SELECT ?county_name ?geo_id\
            WHERE {\
                ?geo_id attribute:name ?county_name . FILTER regex(?geo_id, '/[0-9]{2}$')\
            }\
            ORDER BY ?county_name"):
            county_list.append([row[0], row[1][-2:]])
        
        return county_list

    """ ---------- KOMMUNER ---------- """
    if request.POST:
        initial_letter = request.POST['qstring']
        q = initial_letter
        
        for row in g.query("\
            PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
            SELECT ?o\
            WHERE {\
                ?s attribute:name ?o . FILTER regex(?o, '%s')\
            }\
            ORDER BY ?o" % initial_letter):
            
            """ Order by Scandinavian """
            if row[0].startswith(u'\xc3\x85'):
                c3_85_list.append(row[0])
            elif row[0].startswith(u'\xc3\x84'):
                c3_84_list.append(row[0])
            elif row[0].startswith(u'\xc3\x96'):
                c3_96_list.append(row[0])
            else:
                graph_as_list.append(row[0])

    if request.GET:
        init = request.GET.get('init', '')
        county = request.GET.get('county', '')
        q = request.GET.get('q', '')
        
        #init = request.GET['init']
        
        if init:

            if init == 'all':
                initial_letter = ''
            elif init == u'%c3%85':
                initial_letter = u'\xc3\x85'
            elif init == u'%c3%84':
                initial_letter = u'\xc3\x84'
            elif init == u'%c3%96':
                initial_letter = u'\xc3\x96'
            else:
                initial_letter = init

            for row in g.query("\
                PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
                SELECT ?o\
                WHERE {\
                    ?s attribute:name ?o . FILTER regex(?o, '^%s')\
                }\
                ORDER BY ?o" % initial_letter):
                
                """ Order by Scandinavian """
                if row[0].startswith(u'\xc3\x85'):
                    c3_85_list.append(row[0])
                elif row[0].startswith(u'\xc3\x84'):
                    c3_84_list.append(row[0])
                elif row[0].startswith(u'\xc3\x96'):
                    c3_96_list.append(row[0])
                else:
                    graph_as_list.append(row[0])
                    
        elif county:
            
            for row in g.query("\
                PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
                SELECT ?municipality_name\
                WHERE {\
                    ?municipality_id attribute:name ?municipality_name .\
                    ?municipality_id attribute:county ?county_id . FILTER regex(?county_id, '%s')\
                }\
                ORDER BY ?municipality_name" % county):
                
                """ Order by Scandinavian """
                if row[0].startswith(u'\xc3\x85'):
                    c3_85_list.append(row[0])
                elif row[0].startswith(u'\xc3\x84'):
                    c3_84_list.append(row[0])
                elif row[0].startswith(u'\xc3\x96'):
                    c3_96_list.append(row[0])
                else:
                    graph_as_list.append(row[0])
        
    graph_as_list = graph_as_list + c3_85_list + c3_84_list + c3_96_list
    
    county_list = get_county_list()
    hits = len(graph_as_list)

    return render_to_response('geomaster/kommuner.html', {
        'graph_as_list': graph_as_list,
        'county_list': county_list,
        'hits': hits,
        'q': q
        })

def socknar(request):

    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/parish/parish.rdf") # Socken

    graph_as_list = []
    c3_85_list = [] # u'Å'
    c3_84_list = [] # u'Ä'
    c3_96_list = [] # u'Ö'
    
    
    """ ---------- LANDSKAP ---------- """
    def get_province_list():

        g_province = Graph()
        g_province.parse("http://kulturarvsdata.se/resurser/aukt/geo/province/province.rdf") # Landskap
        province_list = []
        
        for row in g_province.query("\
            BASE <http://kulturarvsdata.se/>\
            PREFIX attribute: <http://kulturarvsdata.se/ksamsok#>\
            SELECT ?province_name ?province_id\
            WHERE {\
                ?province_id attribute:name ?province_name\
            }\
            ORDER BY ?province_name"):
            province_list.append([row[0][0:], row[1][-2:]])
            
        return province_list
        

    """ ---------- SOCKNAR ---------- """
    if request.POST:
        initial_letter = request.POST['qstring']
        q = initial_letter

        for row in g.query("\
            PREFIX attribute: <http://kulturarvsdata.se/ksamsok#>\
            SELECT ?parish_name ?province_id\
            WHERE {\
                ?parish_id attribute:name ?parish_name .\
                ?parish_id attribute:province ?province_id . FILTER regex(?parish_name, '%s')\
            }\
            ORDER BY ?parish_name" % initial_letter):
            
            """ Order by Scandinavian """
            if row[0].startswith(u'\xc3\x85'):
                c3_85_list.append([row[0][0:], row[1][-2:]])
            elif row[0].startswith(u'\xc3\x84'):
                c3_84_list.append([row[0][0:], row[1][-2:]])
            elif row[0].startswith(u'\xc3\x96'):
                c3_96_list.append([row[0][0:], row[1][-2:]])
            else:
                graph_as_list.append([row[0][0:], row[1][-2:]])


    if request.GET:
        init = request.GET.get('init', '')
        province = request.GET.get('province', '')
        q = request.GET.get('q', '')

        if init:

            if init == 'all':
                initial_letter = ''
            elif init == u'%c3%85':
                initial_letter = u'\xc3\x85'
            elif init == u'%c3%84':
                initial_letter = u'\xc3\x84'
            elif init == u'%c3%96':
                initial_letter = u'\xc3\x96'
            else:
                initial_letter = init

            for row in g.query("\
                PREFIX attribute: <http://kulturarvsdata.se/ksamsok#>\
                SELECT ?parish_name ?province_name\
                WHERE {\
                    ?parish_id attribute:name ?parish_name .\
                    ?parish_id attribute:province ?province_name . FILTER regex(?parish_name, '^%s')\
                }\
                ORDER BY ?parish_name" % initial_letter):
                
                """ Order by Scandinavian """
                if  row[0].startswith(u'\xc3\x85'):
                    c3_85_list.append([row[0], row[1][-2:]])
                elif row[0].startswith(u'\xc3\x84'):
                    c3_84_list.append([row[0], row[1][-2:]])
                elif row[0].startswith(u'\xc3\x96'):
                    c3_96_list.append([row[0], row[1][-2:]])
                else:
                    graph_as_list.append([row[0], row[1][-2:]])
                    
                
        elif province:

            for row in g.query("\
                PREFIX attribute: <http://kulturarvsdata.se/ksamsok#>\
                SELECT ?parish_name ?province_name\
                WHERE {\
                    ?parish_id attribute:province ?province_name .\
                    ?parish_id attribute:name ?parish_name . FILTER regex(?province_name, '%s')\
                }\
                ORDER BY ?parish_name" % province):
                
                """ Order by Scandinavian """
                if row[0].startswith(u'\xc3\x85'):
                    c3_85_list.append([row[0], row[1][-2:]])
                elif row[0].startswith(u'\xc3\x84'):
                    c3_84_list.append([row[0], row[1][-2:]])
                elif row[0].startswith(u'\xc3\x96'):
                    c3_96_list.append([row[0], row[1][-2:]])
                else:
                    graph_as_list.append([row[0], row[1][-2:]])
  

    graph_as_list = graph_as_list + c3_85_list + c3_84_list + c3_96_list
    
    province_list = get_province_list()
    hits = len(graph_as_list)

    return render_to_response('geomaster/socknar.html', {
        'graph_as_list': graph_as_list,
        'province_list': province_list,
        'hits': hits,
        'q': q
        })

def lan(request):
    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/county/county.rdf") # Län

    graph_as_list = []
    
    for row in g.query("\
        BASE <http://kulturarvsdata.se/>\
        PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
        SELECT ?o\
        WHERE {\
            ?p attribute:name ?o . FILTER regex(?p, '/[0-9]{2}$')\
        }\
        ORDER BY ?o"):
        graph_as_list.append(row[0])

    return render_to_response('geomaster/lan.html', {'graph_as_list': graph_as_list})


def landskap(request):
    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/province/province.rdf") # Landskap

    graph_as_list = []
    
    for row in g.query("\
        BASE <http://kulturarvsdata.se/>\
        PREFIX attribute: <http://kulturarvsdata.se/ksamsok#>\
        SELECT ?o\
        WHERE {\
            ?s attribute:name ?o\
        }\
        ORDER BY ?o"):
        graph_as_list.append(row[0])

    return render_to_response('geomaster/landskap.html', {'graph_as_list': graph_as_list})
