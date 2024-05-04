from copy import deepcopy
def floodFill(grid,x,y, FillData):
    # Check if a not empty list was provided
    # Two dimensions are preserved for the position. Data kann be any dimensional
    # Check if the starting point is inside the grid
    if not isinstance(grid,list) or len(grid) == 0:
        raise TypeError("Grid must be a non None list with two positional dimensions")
    if not isinstance(grid[0], list):
        raise TypeError("Grid must be a non None list with two positional dimensions")
    if x < 0 or x > len(grid):
        raise ValueError("Starting Position must lie in the grid")
    if y < 0 or y > len(grid[x]):
        raise ValueError("Starting Position must lie in the grid")
    
    # Pre Calculated Neighbouring cells
    neighbours = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    # Set the data to fill to the one of the first one
    Filter = grid[x][y]

    # Create queue
    queue = [x,y]

    # As long as there are elements in the queue
    # For each element in queue set to fill data add neighbours, if they have the same data to queue
    while len(queue) != 0:
        x1, y1 = queue.pop()
        grid[x1][y1] = deepcopy(FillData)
        for x2, y2 in neighbours:
            x3, y3 = x2+x1, y2+y1

            # Skip neighbours, that are outside the grid
            if x3 < 0 and x3 >= len(grid):
                continue
            if y3 < 0 and y3 >= len(grid[x]):
                continue

            # Add cell to queue
            if grid[x3][y3] == Filter:
                queue.append([x3,y3])