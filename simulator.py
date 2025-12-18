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

def draw_roads():
     pygame.draw.rect(screen, ROAD, (CENTER -ROAD_WIDHT//2,0, ROAD_WIDTH, 900))
     pygame.draw.rect(screen, ROAD, (0, CEMNTER -ROAD_WIDTH//2, 900, ROAD_WIDTH))
     pygame.draw.rect(
          screen, JUNCTION,
          (CENTER -ROAD_WIDTH//2, CENTER - ROAD_WIDTH//2, ROAD_WIDTH, ROAD_WIDTH)
     )

def signal_color(lane_name):
     if controller.active_lane==lane_name:
          return Green if controller.blonk_state else RED
     return RED

def draw_signals():
     pygame.draw.circle(screen, signal_color("AL2"), (CENTER - 30, CENTER - 90),10)
     pygame.draw.circle(screen, signal_color("BL2"),(CENTER + 30, CENTER + 90), 10)
     pygame.draw.circle(screen, signal_color("CL2"),(CENTER + 90, CENTER - 30), 10)
     pygame.draw.circle(screen, signal_color("DL2"),(CENTER - 90, CENTER + 30), 10)
     