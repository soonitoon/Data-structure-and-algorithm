from stack_class import stack

def checkBrackets(string):
  brackets_left = ["[","{","("]
  brackets_right = ["]","}",")"]
  str_stack = stack()

  for i in string:
    if i in brackets_left:
      str_stack.push(i)
    
    elif i in brackets_right:
      if str_stack.isEmpty():
        return "여는 괄호 없이 닫는 괄호를 사용했습니다!"
      
      elif brackets_left.index(str_stack.pop()) != brackets_right.index(i):
        return "괄호의 종류가 다릅니다!"
      
  if str_stack.isEmpty() == False:
    return "괄호의 짝이 맞지 않습니다!"
  
  return "이상 없음!"

# statment = """

# (2+1)(*4 + 2

# """

# print(checkBrackets(statment))

def checkBracketsV2():
  file_name = input("검사할 파일명 입력: ")

  with open(file_name, "r", encoding="utf-8") as file_for_check:
    lines = file_for_check.readlines()

  for idx, line in enumerate(lines):
    result = checkBrackets(line)
    print(f"{idx}번째 줄에서", result)

checkBracketsV2()