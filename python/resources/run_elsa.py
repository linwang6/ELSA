#!/usr/bin/python
#' Requiements:
#' 
#' 1. Python 2.7 or greater
#' 2. Packages:
#'    'Python'
#'    numpy (>=1.8.2)
#'    scipy (>=0.13.3)
#'    scikit-learn (>=0.20)
#'    imbalanced-learn (0.4)
#'    pip install -U numpy
#'    pip install -U scipy
#'    pip install -U scikit-learn
#'    pip install -U imbalanced-learn
#'    pip install -U sklearn
#'
#' Please cite our paper if our paper or code helped you.
#'

###################################

import re
import os
import sys
import imp
import argparse
import warnings
import numpy as np

###################################

if len(sys.argv) != 7:
    print """

usage: MarkerCheck.py [-t] [-p] [-o]

arguments:
  -t, --traning           traning prep data
  -p, --prediction        prediction prep data
  -o, --output            output file for cell types


"""

###################################
if len(sys.argv) == 7:
    elsa='/usr/local/bin/python2.7 '+'../resources/elsa.py '+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[6]
    os.system(elsa)

###################################

