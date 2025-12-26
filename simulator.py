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
               elif self.direction =='E': dist = self.x - (lead_veh.x+lead_veh.width)
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
                         self.active_dir=heapq.heappop(pq)[1]

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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Priority Traffic - Right Centric System")
    clock = pygame.time.Clock()
    ctrl = TrafficController()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ctrl.update() # Update Physics/Priority
        draw_simulation(screen, ctrl) # Render Graphics
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()        










