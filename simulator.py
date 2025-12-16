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
          
                


