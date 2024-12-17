import json
from groundscanner.map.segment import Segment


class Map:
    # array from type Segment [][] with name segments with heighth and width 19 and given type Segment  [[]]

    def __init__(self):
        None

    def loadMap(self, size, segments):
        self.segments = segments
        self.size = size
        
        
