import heapq as he
import math
from helpers import Map, show_map, load_map

def shortest_path(maps,start,goal):
    
    cameFrom = {}
    opens = set([start])
    closed = set([])
    
    roads_avail  = list(maps.intersections.keys())
    score_g = {road : float("inf") for road in roads_avail}
    score_g[start] = 0
    score_f = {road: float("inf") for road in roads_avail}
    score_f[start] = calc(maps,start,goal)
    frontier = [(score_f[start], start)]
    
    while opens:
        present = he.heappop(frontier)
       
        if present[1] == goal:
            print("shortest path called")
            reverses = path_reconstruction(cameFrom, present[1])
            reverses.reverse()
            print(reverses)
            return reverses
        
        if present[1] in opens:    
            opens.remove(present[1])
            closed.add(present[1])
        
        for i in maps.roads[present[1]]:
            if i in closed:
                continue
                
            if i not in opens:
                opens.add(i)
            
            trial_gscore = score_g[present[1]] + calc(maps, present[1], i)
            if trial_gscore >= score_g[i]:
                continue
                
            cameFrom[i] = present[1]
            score_g[i] = trial_gscore
            score_f[i] = (calc(maps, i, goal) + score_g[i])
            he.heappush(frontier, (score_f[i], i))
       
    return ("Function Failed!!!!")

def path_reconstruction(cameFrom, present):
    path = []
    path_tot = [present]
    while present in cameFrom:
        present = cameFrom[present]
        path_tot.append(present)     
    return path_tot

def calc(maps, start_node, end_node):
    x = math.pow((maps.intersections[start_node][0] - maps.intersections[end_node][0]),2)
    y = math.pow((maps.intersections[start_node][1] - maps.intersections[end_node][1]),2) 
    dist_node = math.sqrt(x + y)
    return dist_node

