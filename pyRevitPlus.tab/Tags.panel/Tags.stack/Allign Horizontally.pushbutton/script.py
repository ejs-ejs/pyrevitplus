"""
Allign Tags / Spot Elevations horizontally

Allign tags and Spot Elevations horizontally, according to the preselected tag.

TESTED REVIT API: 2020

@ejs-ejs
This script is part of PyRevitPlus: Extensions for PyRevit
github.com/ejs-ejs | @ejs-ejs

--------------------------------------------------------
RevitPythonWrapper: revitpythonwrapper.readthedocs.io
pyRevit: github.com/eirannejad/pyRevit

"""
import os
#from collections import namedtuple

from pyrevit import revit, DB, forms, script

import rpw
from rpw import doc, uidoc, DB, UI

from tags_wrapper import *


#Point = namedtuple('Point', ['X', 'Y','Z'])
cView = doc.ActiveView

Tags = rpw.ui.Selection()

         
if cView.ViewType in [DB.ViewType.FloorPlan, DB.ViewType.CeilingPlan, DB.ViewType.Detail, DB.ViewType.AreaPlan, DB.ViewType.Section, DB.ViewType.Elevation]:
        
    if len(Tags) < 1:
        UI.TaskDialog.Show('pyRevitPlus', 'A tag must preselected')
    if len(Tags) > 1:
        UI.TaskDialog.Show('pyRevitPlus', 'Select a SINGLE tag')
    else:
        cTag = Tags[0]
        if cTag.unwrap().GetType() in [DB.IndependentTag, DB.SpotDimension]:
            if cTag.unwrap().GetType() == DB.IndependentTag:
                cPos = cTag.TagHeadPosition
            else:
                cPos = cTag.Location.Point
    
        with forms.WarningBar(title='Pick tag One by One. ESCAPE to end.'):
            if cView.ViewType in [DB.ViewType.Section, DB.ViewType.Elevation]:
                allign_Z(cTag.Category, cPos)
            else:
                allign_Y(cTag.Category, cPos)
else:
    UI.TaskDialog.Show('pyRevitPlus', 'View type \'{}\' is not supported.'.format(cView.ViewType))
        