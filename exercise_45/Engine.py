from Map import Map
class Engine(Map):
    def start(self):
        Map.NextZone(self, "Maze")

engine = Engine()
engine.start()
