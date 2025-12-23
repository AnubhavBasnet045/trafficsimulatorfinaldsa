import pygame
import sys
import random
import heapq
#----------------------(main)-------------
WIDTH, HEIGHT = 900,900
CENTER = WIDTH //2
ROAD_WIDTH= 300
LANE_WIDTH = 50
STOP_DIST=170

#COLORS
GRASS=(75,125,75)
ROAD=(30,30,30)
LINE_COLOR =( 240,240,240)
RED, GREEN = (255,60,60),(60,255,60)
STRAIGHT_CAR=(70,130,255)
FREE_RIGHT_CAR=(255,100,0)

#----BACKEND---------

class lane:
     def __init__(self, name, direction, base_priority=1):
          self.name=name
          self.queue=deque()
          self.direction= direction
          self.base_priority = base_priority


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
               "AL2": Lane("AL2","down" ,base_priority=2),
               "BL2": Lane("BL2", "up"),
               "CL2": Lane("Cl2", "left"),
               "Dl2": Lane("Dl2", "right"),
          }

         
          self.arrival_counter=0

          self.priority_heap=[]
          self.threshold_reached=set()

          self.active_lane= None



     def generate_traffic(self):
          for name, lane in self.lanes.items():

               if name== self.active_lane:
                    continue
               if random.random() < 0.6:
                    lane.add_vehicle()

               if lane.size()== 10 and name not in self.threshold_reached:
                    self.arrival_counter += 1
                    priority=lane.size()+ lane.base_priority *5

                    heapq.heappush(
                         self.priority_heap,
                         (-priority, self.arrival_counter, name)
                    )          

                    self.threshold_reached.add(name)
     def choose_lane(self):
          if self.active_lane:
               return self.active_lane

          if self.priority_heap:
               _, _, lane_name = heapq.heappop(self.priority_heap)
               self.active_lane=lane_name
               return lane_name

          return None           
     def serve_traffic (self):
          lane_name=self.choose_lane()
          if not lane_name:
               return

          lane = self.lanes[lane_name]
          lane.serve(3)

          if lane.size()==0:
               self.active_lane= None    
                
#-------FRONTEND----------
pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("Traffic Junction")
clock=pygame.time.Clock()

WHITE=(255,255,255)
ROAD=(40,40,40)
JUNCTION=(70,70,70)
LINE=(255,255,255)
RED=(220,60,60)
GREEN=(60,200,60)
CAR=(30,30,200)

controller =TrafficController()

CENTER=450
LANES_PER_ROADS=3
LANE_WIDTH=40
LANES_GAP=10
ROAD_WIDTH=LANES_PER_RAOD * LANE_WIDTH + (LANES_PER_ROAD -1)* LANES_GAP
CAR_GAP=45

def draw_roads():
     pygame.draw.rect(screen, ROAD, (CENTER - ROAD_WIDTH//2,0, ROAD_WIDTH, 900))
     pygame.draw.rect(screen, ROAD, (0, CENTER - ROAD_WIDTH//2, 900, ROAD_WIDTH))
     pygame.draw.rect(
          screen, JUNCTION,
          (CENTER -ROAD_WIDTH//2, CENTER - ROAD_WIDTH//2, ROAD_WIDTH, ROAD_WIDTH)
     )
def draw_lane_lines():
     for i in range(1, LANES_PER_ROAD):
          x=CENTER - ROAD_WIDTH//2 + i* ( LANE_WIDTH + LANE_GAP)-LANE_GAP//2
          y=0
          while y <900:
               if y< CENTER - ROAD_WIDTH //2 or y > CENTER + ROAD_WIDTH//2:
                    pygame.draw.line(screen, LINE, (x,y),(x, y+20),2)
               y+=40
     for i in range(1, Lanes_PER_ROAD):
          y=CENTER- ROAD_WIDTH//2 + i* (LANE_WIDTH + LANE_GAP)-LANE_GAP//2
          x=0
          while x<900:
               if x< CENTER -ROAD_WIDTH //2 or x> CENTER + ROAD_WIDTH//2:
                    pygame.draw.line(screen ,LINE, (x,y),(X+20,y),2)
               x+=40                    
def signal_color(lane_name):
     return GREEN if controller.active_lane == lane_name else RED
def draw_signals():
     pygame.draw.circle(screen, signal_color("AL2"), (CENTER - 40, CENTER - 100),10)
     pygame.draw.circle(screen, signal_color("BL2"),(CENTER + 40, CENTER + 100), 10)
     pygame.draw.circle(screen, signal_color("CL2"),(CENTER + 100, CENTER - 40), 10)
     pygame.draw.circle(screen, signal_color("DL2"),(CENTER - 100, CENTER + 40), 10)

def draw_vehicles():
     for i in range(controller.lanes["AL2"].size()):
          lane= i % LANES_PER_ROAD
          x= CENTER - ROAD_WIDTH //2 + lane *( LANE_WIDTH+ LANE_GAP)+ 5
          y= CENTER -120 - ( i // LANES_PER_ROAD)*CAR_GAP
          pygame.draw.rect(screen,car,(x,y,25,40))

     for i in range(controller.lanes["BL2"].size()):
          pygame.draw.rect(screen, CAR, (CENTER + 5, CENTER +80 + i*CAR_GAP, 25, 40))

     for i in range( controller.lanes["CL2"].size()):
          pygame.draw.rect(screen, CAR, (CENTER + 80 + i*CAR_GAP, CENTER - 20, 40 , 25))

     for i in range(controller.lanes["DL2"].size()):
          pygame.draw.rect(screen, CAR, (CENTER - 120 - i*CAR_GAP, CENTER + 5, 40 , 25)) 

            
     