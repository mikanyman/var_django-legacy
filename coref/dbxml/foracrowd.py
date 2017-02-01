#! /usr/bin/env python

# SOURCE: XML.com / Scaling Up with XQuery, Part 2
# PROBLEM DESCRIBED HERE!
# http://kr.forums.oracle.com/forums/thread.jspa?threadID=712554

from bsddb3.db import *
from dbxml import *

def foracrowd():

    """ ASSIGNING, INSTANTIATING, OPENING """
    mgr = XmlManager()
    qc = mgr.createQueryContext()
    containerName = 'phone.dbxml'
    cont = mgr.openContainer(containerName)


    """ QUERY """
    results = mgr.query("collection('phone.dbxml')/phonebook[name/first = 'Lisa']/phone[@type = 'home']/string()", qc);


    """ OUTPUT """
    results.reset()
    for value in results:
        print value.asString()

if __name__ == "__main__":
    foracrowd()
