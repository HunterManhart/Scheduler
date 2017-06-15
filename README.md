# Scheduler

Using integer linear programming (with gurobi via Pulp) to schedule interviews between students and firms.

## Variables

#### Problem Variables

 - F: Firms
 - S: Students
 - T: Number of timeslots
 - M: Meetings needed (which firms need to meet with which students)
 
#### Linear Variables

 - Possible Slots (FST): Boolean slot for each possible Firm-Student-Timeslot
 
**Number of linear variables: M * T**

## Constraints

 1) Students can only have one interview per timeslot and must have break after
 2) Firms can only have one Student interview per timeslot
 3) A firm-student interview must be in only one timeslot
 
**Number of constraints:**
 1) ~ S * T
 2) ~ F * T
 3) M

### Example Size

S = 25   
F = 14   
T = 20   

Each firm wants to interview about half the students so:  
M = 182  

#### Variables: 3640
M * T = 182 * 20

#### Constraints: 572
(~ 25 * 20) + (~ 14 * 20) + 182   
250 + 140 + 182   

Program does not add a constraint on the ~ approximations if firm-student aren't to have a meeting  
Thus ~ is about half as we determined firms would only want meetings with half the students  
(and just assuming distribution of students among firms is even for ~14*20) 


## Optimization

Attempts to place all meetings in the morning, by weighting timeslots.  
This also optimizes towards minimizing the length of time firms need to spend for interviews.
