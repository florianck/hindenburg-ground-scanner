import json
import rclpy
from rclpy.node import Node
from groundscanner.map.map import Map
from groundscanner.map.segment import Segment
from std_msgs.msg import String


class ScannerNode(Node):
    def __init__(self):
        super().__init__("scanner")

        # create map
        map = Map()

        # load file map.json as string
        with open("map.json") as f:
             json_string = f.read() 
             parsed_data = json.loads(json_string)
             size=parsed_data["arena"]["size"]

             map.loadMap(size=size,segments=[[Segment(**segment) for segment in row] for row in parsed_data["arena"]["segments"]])

        
def main():
    rclpy.init()
    pn = ScannerNode()
    rclpy.spin(pn)
    rclpy.shutdown()

if __name__ == "__main__":
    main()