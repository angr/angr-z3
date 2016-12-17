#!/usr/bin/env python

import os, sys
oldplace = os.getcwd()
place = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src/api/python')
os.chdir(place)
sys.path = [place] + sys.path
import setup
os.chdir(oldplace)
