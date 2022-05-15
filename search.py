# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

   # Contains the already discovered coordinates
    discovered = []

   # Contains Directions [NORTH, SOUTH, WEST, ...]
    path = []

   # Each stack element contains a coordinate and a path from the starting point to the coordinate ((x,y), (NORTH, SOUTH, WEST, ...))
    st = Stack
    st.__init__(st)
    st.push(st, (problem.getStartState(), path))

    if problem.isGoalState(problem.getStartState()):
       return []

   # The actual DFS algorithm
    while not st.isEmpty(st):
       node, path = st.pop(st)

       if problem.isGoalState(node):
           return path

       if node not in discovered:
           discovered.append(node)
           succ = problem.getSuccessors(node)
           for state in succ:
               if state[0] not in discovered:
                   updated_path = path + [state[1]]
                   st.push(st, (state[0], updated_path))

    return path
   #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from util import Queue
    
    discovered = []
    
    path = []
    
    q = Queue
    q.__init__(q)
    q.push(q, (problem.getStartState(), path))
    
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not q.isEmpty(q):
        node, path = q.pop(q)
        
        if problem.isGoalState(node):
            return path
        
        if node not in discovered:
            discovered.append(node)
            succ = problem.getSuccessors(node)
            for state in succ:
                if state[0] not in discovered:
                    updated_path = path + [state[1]]
                    q.push(q, (state[0], updated_path))
    
    return path
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    from util import PriorityQueue
    
    discovered = []
    path = []
    
    pq = PriorityQueue
    pq.__init__(pq)
    pq.push(pq, (problem.getStartState(), path), 0)
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not pq.isEmpty(pq):
        node, path = pq.pop(pq)
        
        if problem.isGoalState(node):
            return path
        
        if node not in discovered:
            discovered.append(node)
            succ = problem.getSuccessors(node)
            
            for state in succ:
                if state[0] not in discovered:
                   updated_path = path + [state[1]]
                   
                   priority = problem.getCostOfActions(updated_path)
                   
                   pq.push(pq, (state[0], updated_path), priority)
                   
                elif state[0] not in discovered:
                    for state in pq.heap:
                        if state[2][0] == state[0]:
                            old_priority = problem.getCostOfActions(state [2][1])
                    
                    new_priority = problem.getCostOfActions(path + [state[1]])
                    
                    if old_priority > new_priority:
                        updated_path = path + [state[1]]
                        pq.update(pq, (state[0], updated_path), new_priority)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
