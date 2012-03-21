from GoTools import *
from epydoc.docbuilder import build_doc_index
from epydoc.docwriter.html import HTMLWriter
from epydoc.docwriter.latex import LatexWriter

doxy = build_doc_index(['GoTools', \
                        'GoTools.Curve', \
                        'GoTools.Surface', \
                        'GoTools.VolumeFactory', \
                        'GoTools.CurveFactory', \
                        'GoTools.SurfaceFactory', \
                        'GoTools.SurfaceModelFactory'],introspect=True,parse=True)
l = LatexWriter(doxy)
l.write('doc/latex/')

h = HTMLWriter(doxy)
h.write('doc/html/')