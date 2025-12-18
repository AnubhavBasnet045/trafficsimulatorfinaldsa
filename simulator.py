from collections import deque
#----BACKEND---------

class lane:
     def __init__(self, name, direction):
          self.name=name
          self.queue=deque()
          self.direction= direction

          def add_vehicle(self):
               self.queue.append(1)
def serve(self, count):
        for _ in range(min(count, len(self.queue))):
            self.queue.popleft()

            def size(self):
                 return len(self.queue)
            

class TrafficController:
     def __init__(self):
          self.lanes={
               "AL2": Lane("AL2","down"),
               "BL2": Lane("BL2", "up"),
               "CL2": Lane("Cl2", "left"),
               "Dl2": Lane("Dl2", "right"),
          }

          self.current_green=None

          self.threshold_queue= deque()
          self.threshold_reached=set()

          self.active_lane= None


          self.blink_state = True
          self.blink_timer=0
          
                
#-------FRONTEND----------
pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("Traffic Junction with Priority Queue")
clock=pygame.time.Clock()

WHITE=(255,255,255)
ROAD=(40,40,40)
JUNCTION=(70,70,70)
RED=(220,60,60)
GREEN=(60,200,60)
CAR=(30,30,200)

controller =TrafficController()

CENTER=450
ROAD_WIDTH=140
CAR_GAP=45


