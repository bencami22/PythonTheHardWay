from Maze import Maze
from TreasureArea import TreasureArea
from DeathPit import DeathPit
from Zone import Zone

class Map(Zone):
    zones = {
    "Maze" : Maze(),
    "TreasureArea" : TreasureArea(),
    "DeathPit" : DeathPit()
    }

    current_zone = None

    def __init__(self):
        pass

    def NextZone(self, zone):
        #print("zone=", zone)
        next_zone = zone
        if next_zone != None:

            super().changing_zone(self.current_zone, zone)
            self.current_zone = zone
            next_zone = self.zones.get(zone).play()
            self.NextZone(next_zone)
