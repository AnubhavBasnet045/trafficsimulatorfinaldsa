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

class Vehicle:
     def __init__(self, direction,lane_index):
          self.direction= direction
          self.lane_index=lane_index
          self.speed = 2
          self.width, self.height =(28, 45) if direction in ['N','S'] else (45, 28)

#----------position logic-----------------
          if direction =='N':
               self.x=(CENTER + ROAD_WIDTH //2)-((2-lane_index)*LANE_WIDTH)-40
               self.y=-50
          elif direction =='S':
               self.x=(CENTER- ROAD_WIDTH //2)+((2-lane_index)*LANE_WIDTH)+ 10
               self.y = HEIGHT + 50
          elif direction =='E':
               self.y =(CENTER + ROAD_WIDTH//2)-((2-lane_index)*LANE_WIDTH)-40
               self.x = WIDTH + 50
          elif direction =='W':
               self.y =(CENTER - ROAD_WIDTH//2)+((2-lane_index)*LANE_WIDTH)+10
               self.x = -50          
     
     def move ( self , is_green, lead_veh):
          if self.lane_index ==2:
               self._execute_free_right()
               return 
          
          stop = False
          if not is_green:
               if self.direction =='N'and CENTER - STOP_DIST <self.y+self.height<CENTER -STOP_DIST + 10 : stop = True
               elif self.direction =='S'and CENTER + STOP_DIST -10<self.y< CENTER +STOP_DIST: stop = True
               elif self.direction =='E'and CENTER + STOP_DIST -10<self.x< CENTER +STOP_DIST: stop = True
               elif self.direction == 'W'and CENTER - STOP_DIST < self.x +self.width < CENTER- STOP_DIST+ 10: stop = True

          if lead_veh:
               dist =0
               if self.direction =='N': dist = lead_veh.y - ( self.y + self. height)
               elif self.direction =='S': dist = self.y -(lead_veh.y+lead_veh.height)
               elif self.direction ==' E': dist = self.x - (lead_veh.x+lead_veh.width)
               elif self.direction =='W': dist = lead_veh.x- (self.x+ self.width)
               if 0 < dist< 30 : stop = True

          if not stop :
               if self.direction =='N': self.y += self.speed
               elif self.direction =='S': self.y -=self.speed
               elif self.direction =='E': self.x -= self.speed
               elif self.direction =='W':self.x += self.speed
     def _execute_free_right(self):
          tp= 145
          if self.direction == 'N':
               if self.y<CENTER - tp : self.y+=self.speed
               else:self.x+=self.speed; self.width, self.height= 45,28
          elif self.direction=='S':
               if self.y>CENTER + tp : self.y -= self.speed
               else: self.x-=self.speed; self.width, self.height = 45,28
          elif self.direction=='E':
               if self.x>CENTER + tp : self.x -= self.speed
               else: self.y += self.speed; self.width, self.height = 28,45
          elif self.direction == 'W':
               if self.x<CENTER - tp : self.x += self.speed
               else: self.y-=self.speed; self.width, self.height = 28,45

     class TrafficController:
          def __init__(self):
               self.lanes={d:{0:[],1:[],2:[]}for d in [ 'N','S','E','W']}
               self.active_dir='N'
               self.timer=0

          def update(self):
               self.timer+=1

               if random.random()<0.05:
                    d=random.choice(['N','S','E','W'])
                    l=random.choice([0,1,2])
                    self.lanes[d][l].append(Vehicle(d,l))     
                    
     #Priority queue logic

               if self.timer >240 or (len(self.lanes[self.active_dir][0])+len(self.lanes[self.active_dir][1])==0):
                    self.timer=0
                    pq=[]
                    for d in ['N','S','E','W']:
                         waiting =len(self.lanes[d][0])+len(self.lanes[d][1])
                         heapq.heappush(pq,(-waiting,d))

                    if pq:
                         self.active_dir=heapq.heapq.heappop(pq)[1]

                    for d in ['N','S','E','W']:
                         for l in [0,1,2]:
                              for i , v in enumerate(self.lanes[d][l]):
                                   lead=self.lanes[d][l][i-1] if i>0 else None 
                                   v.move(self.active_dir==d,lead)

                              self.lanes[d][l]=[v for v in self.lanes[d][l] if - 120< v.x<WIDTH+120 and -120< v.y< HEIGHT + 120]

#-------FRONTEND----------
def draw_simulation(screen,ctrl):
     screen.fill(GRASS)

     # Roads

     pygame.draw.rect(screen,ROAD,(CENTER- ROAD_WIDTH//2,0,ROAD_WIDTH,HEIGHT))
     pygame.draw.rect(screen,ROAD,(0, CENTER - ROAD_WIDTH//2,WIDTH,ROAD_WIDTH))

     #divider
     pygame.draw.line(screen,(255, 215,0),(CENTER,0),(CENTER, HEIGHT),3)
     pygame.draw.line(screen,(255,215,0),(0, CENTER),(WIDTH,CENTER),3)
     
     #DRAW lane dashes
     for i in [-1,1]:
          for pos in range(0,900,40):
               pygame.draw.line(screen, LINE_COLOR,(CENTER + i*50,pos),(CENTER + i*50,pos+20),1)
               pygame.draw.line(screen,LINE_COLOR,(pos, CENTER + i*50),(pos+20, CENTER+ i*50),1)

      #draw signal

     sig_pos={'N':(CENTER+170,CENTER-170),'S':(CENTER -170,CENTER+170),'E':(CENTER+ 170,CENTER + 170),'W':(CENTER - 170,CENTER - 170)}
     for d, p in sig_pos.items():
          color=GREEN if ctrl.active_dir==d else RED
          pygame.draw.circle(screen, color,p,20)

     #draw vehicle
     for d in ctrl.lanes:
          for l in ctrl.lanes[d]:
               for v in ctrl.lanes[d][l]:
                    color = FREE_RIGHT_CAR if v.lane_index ==2 else STRAIGHT_CAR
                    pygame.draw.rect(screen, color,(v.x , v.y, v.width, v.height), border_radius=4)

#main loop

def main():
     pygame.init()
     screen=pygame.display.set_mode((WIDTH,HEIGHT))
     pygame.display.set_caption("Priority Traffic - Right Centric System")
     clock = pygame.time.Clock()

     ctrl = TrafficController()
     













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

            
     