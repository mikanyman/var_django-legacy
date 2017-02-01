# dbxml/views.py

from django.shortcuts import render_to_response
import os
from bsddb3.db import *
from dbxml import *

def index(request, xquery):
    pass

def crowd(request):
    """ dbxml wrapper """

    dbxml_py = '/home/cidoc/crowd.py'
    
    file = os.popen(dbxml_py)
    
    data = file.readlines() # creates list
    
    #data = ''
    #for line in file.readlines():
    #    data.append(line)
    
    file.close()
    
    context = {'query_result': data}
    return render_to_response('dbxml/index.html', context)


#How do I read a huge file line by line in Python, 
#without loading the entire thing into memory first?
#http://www.yak.net/fqa/171.html

#http://cidoc.coreference.org/dbxml/pytest/07/
