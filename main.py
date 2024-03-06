maze = [["🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫"], 
        ["🟫", "🟫", "🟦", "🟫", "🟦", "🟦", "🟦", "🟫", "🟫"],
        ["🟫", "🟫", "🟦", "🟫", "🟫", "🟫", "🟦", "🟦", "🟫"], 
        ["🟫", "🟦", "🟦", "🟫", "🟫", "🟫", "🟫", "🟦", "🟦"],
        ["🟫", "🟦", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟦"], 
        ["🟦", "🟦", "🟦", "🟦", "🟦", "🟫", "🟫", "🟫", "🟨"],
        ["🟫", "🟦", "🟫", "🟫", "🟦", "🟫", "🟫", "🟫", "🟦"], 
        ["🟫", "🟦", "🟫", "🟫", "🟦", "🟫", "🟫", "🟦", "🟦"],
        ["🟫", "🟦", "🟫", "🟫", "🟦", "🟫", "🟦", "🟦", "🟫"],
        ["🟫", "🟦", "🟫", "🟦", "🟦", "🟦", "🟦", "🟫", "🟫"],
        ["🟫", "🟦", "🟦", "🟦", "🟫", "🟫", "🟫", "🟫", "🟫"]]
endChar = "🟨"
wallChar = "🟫"



def isPositionValid(maze, visited, coords):
    x = coords[0]
    y = coords[1]
    maxX = len(maze[0])
    maxY = len(maze)
    if x < maxX and y < maxY and x >= 0 and y >= 0 and visited.count([x, y]) == 0 and maze[y][x] != wallChar: 
        return True
    return False

def displayMaze(maze):
    for row in maze:
        line = ""
        for c in row:
            line += c
        print(line)
        
def isEnd(maze, coords):
    x = coords[0]
    y = coords[1]
    if maze[y][x] == endChar:
        return True
    return False

def replaceCoords(maze, coordArray, newChar):
    for coords in coordArray:
        maze[coords[0]][coords[1]] = newChar

def solveMaze(maze, coords):
    queue = [coords]
    visited = [coords]
    paths = {}
    currentPos = [-1, -1]
    while queue != []:
        currentPos = queue.pop(0)
        x = currentPos[0]
        y = currentPos[1]

        if isEnd(maze, [x, y]):
            break

        if isPositionValid(maze, visited, [x + 1, y]):
            paths[f"{x + 1},{y}"] = [x, y]
            queue.append([x + 1, y])
            visited.append([x + 1, y])
        
        if isPositionValid(maze, visited, [x - 1, y]):
            paths[f"{x - 1},{y}"] = [x, y]
            queue.append([x - 1, y])
            visited.append([x - 1, y])
        
        if isPositionValid(maze, visited, [x, y + 1]):
            paths[f"{x},{y + 1}"] = [x, y]
            queue.append([x, y + 1])
            visited.append([x, y + 1])

        if isPositionValid(maze, visited, [x, y - 1]):
            paths[f"{x},{y - 1}"] = [x, y]
            queue.append([x, y - 1])
            visited.append([x, y - 1])

    path = []
    while currentPos != coords:
        x = currentPos[0]
        y = currentPos[1]
        path.append([y, x])
        currentPos = paths[f"{x},{y}"]
    path.append([currentPos[1], currentPos[0]])
    return path

solutionPath = solveMaze(maze, [0, 5])


replaceCoords(maze, solutionPath, "🟥")
displayMaze(maze)