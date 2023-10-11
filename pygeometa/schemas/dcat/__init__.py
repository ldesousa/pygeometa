# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution # is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2020 Tom Kralidis, Paul van Genuchten
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import json
import os

from rdflib import Graph, Literal
from rdflib.namespace import DCAT, RDF

from pygeometa.helpers import json_serial
from pygeometa.schemas.base import BaseOutputSchema

THISDIR = os.path.dirname(os.path.realpath(__file__))


class DCATOutputSchema(BaseOutputSchema):
    """dcat output schema"""

    def __init__(self):
        """
        Initialize object

        :returns: pygeometa.schemas.base.BaseOutputSchema
        """

        super().__init__('dcat', 'json', THISDIR)


    def addDataProperty(instance, dict):
       
       return


    def write(self, mcf: dict) -> str:
        """
        Write outputschema to JSON string buffer

        :param mcf: dict of MCF content model

        :returns: MCF as a dcat representation
        """

        print("Keys present in dict: " + str(mcf.keys()))
        print("Keys in mcf: " + str(mcf['mcf'].keys()))

        print(str(mcf["identification"]["abstract"]))
        print(str(mcf["identification"]["title"]))
        #print(str(mcf["identification"]["doi"]))
        print(str(mcf["identification"]["keywords"]))
        print(str(mcf["identification"]["url"]))
        #print(str(mcf["identification"]["language"]))

        # Read in CSV map
        w3c = pandas.read_csv('MapW3C.csv')

        # Next:
        # https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html    
        grph = Graph()

        grph.add((mcf["metadata"]["dataseturi"], RDF.type, DCAT.Dataset ))

        for key in mcf["metadata"]:
            node = mcf["metadata"][key]
            if node is dict:
                print("Key to dictionary: " + str(mcf[key]))
            else:
                row = w3c.loc[df["Parent"] == key]
                if row != None:
                      if row["DataProperty"] != None:
                        ont, prop = row["DataProperty"].split(":")
                      prop = URIRef()
                      type_uri = URIRef()
                      lit = Literal(node, datatype=type_uri) 
                      grph.add((mcf["metadata"]["dataseturi"], prop ,lit))

        print(grph.serialize())

