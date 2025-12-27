**TRAFFIC INSERTION SIMULATION: DOCUMENTATION**

**TITLE**
.Assignment:Priority-Based Traffic Simulation system
.Name: Anubhav Basnet
.Roll Number: 09

**SUMMARY OF WORK**
I have developed a real- time traffic insertion simulator using Python and Pygame. 
Key features include:
1. Free left turns: Vehicle in the leftmost lane can turn left without waiting for a signal.
2. Dynamic Signal Control: Insted of a fixed timer, the traffic lights are controlled by a priority based logic that clears the busiest lane first.
3. Collision Avoidance: A queue-based distance checking algorithm ensures vehicles maintain a safe gap and donot overlap while waiting or moving.

**DATA STRUCTRURES**
The simulation relies on two primary data structure to manage the flow and ordering of vehicles.
1. Queue(FIFO):
   Implementation: Python list objects stored in a dictionary: self.lanes[direction][lane].
   Purpose:Manages the order of vehicles in each lane. Ensure the first vehicle to arrive at the insertion is the first to leave(First in , First out).

2. Priority Queue:
   Implementation: Python heapq module (Min Heap).
   Purpose:Determine which of the four road direction (N,S,E,W)should receive a green light based on the highest vehicle count.

**LIST OF FUNCTIONS USING DATA STRUCTURES**
1. TrafficController.__init__:
   Initialize the dictionary of lists (Queues)for all 12 lanes(3 lanes per 4           directions).      
2. TrafficController.update:
   Uses list.oppend() to enqueue new vehicles.
   Uses heapq.heappush and heapq.heappop to calculate and switch the active green light direction.
   Uses list comprehension to 'dequeue' vehicles once they leave the screen boundaries.
3. Vehicle.move:   
   Accesses the lane queue to identify the lead_veh(the vehicle directly in front) to calculate safety distances.


**ALGORITHM FOR TRAFFIC PROCESSING**
The simulation uses a Houristic Based Priority Switching algorithm:
1. State monitoring:
   Every frame, the TrafficController monitors the lenght of each lane queue.

2. Wait Condition:
A signal switch is triggered if either the current green light  timer exceeds 240 frames or the current green lanes become empty.

3. Priority Calculation:
For each direction, it calculates a 'Priority Score' by summing the number of vehicles in the signal-controlled lanes(Lanes 0 and 1).

4. Selection:
The direction with the maximum score is selected using a Max-Priority Queue implementation.

5. Execution:
The selected direction turns green, and vehicle move according to FIFO order within their specific lane queues.


**TIME COMPLEXITY ANALYSIS**
1. Vehicle Spawn--O(1)--Adding a vehicle to the end of a list is a constant time operation.

2. Collision Check -- O(N) -- In each frame, every vehicle checks the position of the one vehicle directly in    front ot it. Since there are N total vehicles, this is linear.

3. Priority Switching -- O(D log D) -- Where D is the number of direction . Building the heap and popping the max takes logarithmic time relative to directions.

4. Total frame updates -- O(N)--Since D is a small constant, the overall time complexity per frame is dominated by the number of vehicle N corrently on the screen.


**SOURCE CODE:**
The complete source code for this simulation, including the backend logic and the pygame-based frontend can be found at the link below:
https://github.com/AnubhavBasnet045/trafficsimulatorfinaldsa.git
**ScreenRecord**
https://github.com/user-attachments/assets/761d54f6-8884-43ff-a5f7-f2007d521735


   
