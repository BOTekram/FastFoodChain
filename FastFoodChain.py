'''
Author: Ekramul Islam
ID: 33275548
Unit: FIT2004 Algorithms and Data Structures
Assignment 1
'''

#Question 1: Fast Food Chain

def restaurantFinder(d, site_list):
    """
    Function description:
    This function finds the maximum revenue possible by opening restaurants 
    at certain sites, obeying the constraint that no two restaurants can be within
    'd' sites of each other.
    
    Approach description:
    Dynamic Programming is used to keep track of the maximum revenue for each site 
    
    :Input:
        d: An integer representing the minimum distance between restaurants.
        site_list: A list of integers where each integer represents the revenue at that site.
        
    :Output, return or postcondition:
        Returns a tuple containing the maximum revenue and the list of sites selected.
        
    :Time complexity:
        O(N), where N is the length of site_list, representing the number of potential restaurant sites.
        
    :Aux space complexity:
        O(N), where N is the length of site_list, representing the number of potential restaurant sites.
    """

    # Number of sites
    N = len(site_list)
    
    # Initialize an array to store maximum revenue for each site
    max_revenue = [0] * N
    
    # Initialize an array to store the sites selected to achieve max revenue for each site
    selected_sites_for_max_revenue = [[] for _ in range(N)]
    
    # Iterate through each site
    for i in range(N):
        # Case 1: Don't open restaurant at this site
        if i == 0:
            case_1_revenue = 0 # No revenue
            case_1_sites = [] # No sites selected
        else: 
            case_1_revenue = max_revenue[i-1] # Max revenue at the previous site
            case_1_sites = selected_sites_for_max_revenue[i-1][:] # Copy the list of selected sites from the previous site
        
        # Case 2: Open restaurant at this site
        if i - d - 1 >= 0:
            case_2_revenue = site_list[i] + max_revenue[i - d - 1] # Add the revenue at this site to the max revenue at the site d sites before this one
            case_2_sites = selected_sites_for_max_revenue[i - d - 1] + [i+1] # Add this site to the list of selected sites
        else:
            case_2_revenue = site_list[i] # No previous site to consider
            case_2_sites = [i+1] # Add this site to the list of selected sites
        
        # Choose the better case
        if case_1_revenue > case_2_revenue:
            max_revenue[i] = case_1_revenue # Max revenue at this site is the same as the max revenue at the previous site
            selected_sites_for_max_revenue[i] = case_1_sites # List of selected sites is the same as the list of selected sites at the previous site
        else:
            max_revenue[i] = case_2_revenue # Max revenue at this site is the revenue at this site plus the max revenue at the site d sites before this one
            selected_sites_for_max_revenue[i] = case_2_sites # List of selected sites is the list of selected sites at the site d sites before this one plus this site
    
    return (max_revenue[-1], selected_sites_for_max_revenue[-1]) # Return the max revenue and the list of selected sites





#--------------------------------------------- 

#Question 2 Climb King


class FloorGraph:
    """
    Class description:
    This class represents a floor in the tower, where each floor is represented as a graph.
    The graph contains vertices (locations), edges (paths between locations), and keys.
    """

    def __init__(self, paths, keys):
        """
        Function description:
        Initializes the graph with the given paths and keys.
        
        :Input:
            paths: A list of tuples (u, v, x) representing edges from u to v with weight x.
            keys: A list of tuples (k, y) representing keys at location k with a time y to defeat the monster.
            
        :Time complexity:
            O(|V| + |E|), where |V| is the set of unique locations in the paths and |E| is the set of edges (paths).
            
        :Aux space complexity:
            O(|V| + |E|), where |V| is the set of unique locations in the paths and |E| is the set of edges (paths).
        """
        self.max_vertex = max(max(u, v) for u, v, _ in paths) # Get the maximum vertex number
        self.graph = [[] for _ in range(self.max_vertex + 1)] # Initialize the graph
        self.keys = [-1] * (self.max_vertex + 1) # Initialize the keys
        
        # Add all paths to the graph
        for u, v, x in paths:
            self.graph[u].append((v, x))

        # Add all keys to the graph
        for k, y in keys:
            self.keys[k] = y

    def climb(self, start, exits):
        """
        Function description:
        Finds the shortest route from the start to one of the exit points, ensuring that a key is collected.
        
        :Input:
            start: The starting point in the floor.
            exits: A list of exit points in the floor.
            
        :Output, return or postcondition:
            Returns a tuple containing the total time and the shortest route as a list of integers.
            
        :Time complexity:
            O(|E| log |V|), where |E| is the set of edges connecting the locations and |V| is the set of unique locations on the floor.
            
        :Aux space complexity:
            O(|V| + |E|), where |V| is the set of unique locations on the floor and |E| is the set of edges connecting these locations.
        """
        # Initialize priority queue with (distance, vertex, has_key, path)
        pq = [(0, start, False, [start])]
        
        visited_with_key = [False] * (self.max_vertex + 1) # Initialize visited with key
        visited_without_key = [False] * (self.max_vertex + 1) # Initialize visited without key
        
        while pq:
            # Sort the priority queue to get the smallest distance first
            pq.sort()
            current_dist, current_node, current_has_key, path_so_far = pq.pop(0) 
            
            # Check if this node is an exit and we have a key
            if current_node in exits and current_has_key:
                return current_dist, path_so_far
            
            # To prevent revisiting the same node with the same state (having a key or not)
            if current_has_key and visited_with_key[current_node]:
                continue 
            if not current_has_key and visited_without_key[current_node]:
                continue
            
            if current_has_key: # Mark as visited with key
                visited_with_key[current_node] = True
            else: # Mark as visited without key
                visited_without_key[current_node] = True
            
            # If a key exists at the current node, add the time to defeat the monster
            if self.keys[current_node] != -1:
                new_dist = current_dist + self.keys[current_node] # Calculate the new distance
                new_path = path_so_far # No need to add the current node to the path
                pq.append((new_dist, current_node, True, new_path)) # Add the current node to the priority queue
            
            # Add all neighbors to the priority queue
            for neighbor, weight in self.graph[current_node]:
                alt = current_dist + weight # Calculate the distance to the neighbor
                pq.append((alt, neighbor, current_has_key, path_so_far + [neighbor])) # Add the neighbor to the priority queue
        
        return None




if __name__ == "__main__":
    
    #Q1 test--------------------------------------------------------------------------------
    # Test the function with example inputs

    print(restaurantFinder(1,[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]))
    print(restaurantFinder(2,[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]))
    print(restaurantFinder(3,[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]))
    print(restaurantFinder(7,[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]))
    print(restaurantFinder(0,[50, 10, 12, 65, 40, 95, 100, 12, 20, 30]))
    
    #Q2.1 test--------------------------------------------------------------------------------
    # Example usage with print statement for output

    paths = [(0, 1, 4), (0, 3, 2), (0, 2, 3), (2, 3, 2), (3, 0, 3)]
    keys = [(0, 5), (3, 2), (1, 3)]
    my_floor = FloorGraph(paths, keys)

    # Assuming start is at node 0 and possible exits are at nodes 1, 2, and 3

    start = 0
    exits = [1, 2, 3]

    path, time_taken = my_floor.climb(start, exits)
    print(f"The optimal path is {path} and it will take {time_taken} minutes.")

    # Test the FloorGraph class---------------------------------------------------------------

    paths = [(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2),
             (5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2),
             (8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)]
    keys = [(5, 10), (6, 1), (7, 5), (0, 3), (8, 4)]
    myfloor = FloorGraph(paths, keys)
    
    # Example 1.1
    print(myfloor.climb(1, [7, 2, 4]))
    # Example 1.2
    print(myfloor.climb(7, [8]))
    # Example 1.3
    print(myfloor.climb(1, [3, 4]))
    # Example 1.4
    print(myfloor.climb(1, [0, 4]))
    # Example 1.5
    print(myfloor.climb(3, [4]))

