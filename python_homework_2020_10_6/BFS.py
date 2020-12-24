from circularQ_practice import CircularQueue
import time

queue = CircularQueue()

def check_position(new_y, new_x):
  if -1 < new_y < 6 and -1 < new_x < 6:
    if map[new_y][new_x] != '1' and map[new_y][new_x] != '.':
      queue.enqueue((new_y, new_x))

def BFS():
  print("start BFS...")
  start = (1, 0)
  queue.enqueue(start)

  while True:
    time.sleep(1) # just kidding :D
    
    current_position = queue.dequeue()
    y, x = current_position[0], current_position[1]
    print("current position :", current_position, end=" ")

    if map[y][x] == 'x':
      print("탐색 성공")
      break

    else:
      map[y][x] = "."

      check_position(y-1, x)
      check_position(y+1, x)
      check_position(y, x-1)
      check_position(y, x+1)
    
    print("queue list : ", queue.display())
  
  time.sleep(1)
  print("quit BFS...")

map = [
  ['1','1','1','1','1','1'],
  ['e','0','1','0','0','1'],
  ['1','0','0','0','1','1'],
  ['1','0','1','0','1','1'],
  ['1','0','1','0','0','x'],
  ['1','1','1','1','1','1']
]

BFS()