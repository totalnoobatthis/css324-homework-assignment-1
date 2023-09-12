def initial_state():
    return (8, 0, 0)

def is_goal(s):
    x,y,z = s
    if x == 4 and y == 4:
        return True
    return False

def successors(s):
    x, y, z = s
    
    #pour x to y
    n = 5 - y
    if n > 0 and x > 0:
        if x > n:
            yield ((x-n, 5, z), n)
        else:
            yield ((0, y+x , z), x)

    #pour x to z
    n = 3 - z
    if n > 0 and x > 0:
        if x > n:
            yield ((x-n , y, 3), n)
        else:
            yield ((0, y, z+x), x)
    
    #pour y to x
    n = 8 - x
    if n > 0 and y > 0:
        if y > n:
            yield ((8, y-n, z), n)
        else:
            yield ((x+y, 0, z), y)

    #pour y to z
    n = 3 - z
    if n > 0 and y > 0:
        if y > n:
            yield ((x, y-n, 3), n)
        else:
            yield ((x, 0, z+y), y)

    #pour z to x
    n = 8 - x
    if n > 0 and z > 0:
        if z > n:
            yield ((8, y, z-n), n)
        else:
            yield ((x+z, y, 0), z)

    #pour z to y
    n = 5 - y
    if n > 0 and z > 0:
        if z > n:
            yield ((x, 5, z-n), n)
        else:
            yield ((x, y+z, 0), z)