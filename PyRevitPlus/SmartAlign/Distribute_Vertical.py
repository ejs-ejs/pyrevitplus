"""
Copyright (c) 2014-2016 Gui Talarico

Smart Align
Smart Align is part of PyRevit Plus Optional Extensions for PyRevit
github.com/gtalarico | gtalarico@gmail.com

--------------------------------------------------------
pyRevit Notice:
pyRevit: repository at https://github.com/eirannejad/pyRevit

"""

__author__ = 'Gui Talarico | gtalarico@gmail.com'
__version = '0.4.0'

import sys
import os
sys.path.append(os.path.dirname(__file__))
from Distribute import main
from core import Align, verbose

if not verbose:
    __window__.Close()

# ALIGN = Align.HDIST
ALIGN = Align.VDIST
main(ALIGN)