from stack_class import stack

DFS_stack = stack()

def test_rute(y, x):
    if 6 > y > -1 and 6 > x > -1:
        if maze[y][x] == "0" or maze[y][x] == "x":
            DFS_stack.push((y,x))

def DFS():
    DFS_stack.push((1,0))

    while not DFS_stack.isEmpty():
        here = DFS_stack.pop()
        print("현재위치 : ",here, end="-->")
        (y_pos, x_pos) = here

        if maze[y_pos][x_pos] == "x":
            break
           
        else:
            maze[y_pos][x_pos] = "."

            test_rute(y_pos-1,x_pos)
            test_rute(y_pos+1,x_pos)
            test_rute(y_pos,x_pos-1)
            test_rute(y_pos,x_pos+1)

        print("스택: ", DFS_stack.top)
    print("탐색 성공" if here == (3,5) else "탐색실패")

maze =[
    ["1", "1", "1", "1", "1", "1"],
    ["e", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "0", "1", "1"],
    ["1", "1", "1", "0", "0", "x"],
    ["1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1"]
]


DFS()