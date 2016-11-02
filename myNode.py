"""
Nodes
file: myNode.py
author: Sean Strout
author: Arthur Nunes-Harwitt
"""

from rit_lib import *


class Node(struct):
    _slots = ((object, 'data'), ((NoneType, 'Node'), 'next') )
    
