**TRAFFIC INSERTION SIMULATION: DOCUMENTATION**

TITLE
.Assignment:Priority-Based Traffic Simulation system
.Name: Anubhav Basnet
.Roll Number: 09

SUMMARY OF WORK
I have developed a real- time traffic insertion simulator using Python and Pygame. 
Key features include:
1. Free left turns: Vehicle in the leftmost lane can turn left without waiting for a signal.
2. Dynamic Signal Control: Insted of a fixed timer, the traffic lights are controlled by a priority based logic that clears the busiest lane first.
3. Collision Avoidance: A queue-based distance checking algorithm ensures vehicles maintain a safe gap and donot overlap while waiting or moving.

DATA STRUCTRURES
The simulation relies on two primary data structure to manage the flow and ordering of vehicles.
1. Queue(FIFO):
   Implementation: Python list objects stored in a dictionary: self.lanes[direction][lane].
   Purpose:Manages the order of vehicles in each lane. Ensure the first vehicle to arrive at the insertion is the first to leave(First in , First out).

2. Priority Queue:
   Implementation: Python heapq module (Min Heap).
   Purpose:Determine which of the four road direction (N,S,E,W)should receive a green light based on the highest vehicle count.

LIST OF FUNCTIONS USING DATA STRUCTURES
1. TrafficController.__init__:
   Initialize the dictionary of lists (Queues)for all 12 lanes(3 lanes per 4           directions).      
2. TrafficController.update:
   Uses list.oppend() to enqueue new vehicles.
   Uses heapq.heappush and heapq.heappop to calculate and switch the active green light direction.
   Uses list comprehension to 'dequeue' vehicles once they leave the screen boundaries.
3. Vehicle.move:   
   Accesses the lane queue to identify the lead_veh(the vehicle directly in front) to calculate safety distances.


ALGORITHM FOR TRAFFIC PROCESSING
The simulation uses a Houristic Based Priority Switching algorithm:
1. State monitoring:
   Every frame, the TrafficController monitors the lenght of each lane queue.

2. Wait Condition:A signal switch is triggered if either the current green light  timer exceeds 240 frames or the current green lanes become empty.

3. Priority Calculation:
   
