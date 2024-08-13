cards = ["two", "three", "four", "five", "six", "seven", "eight", "eight",
         "nine", "ten", "jack", "queen", "king", "ace"]
drews = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
state = 0
stack = 0
turn = -1
a = 0
b = 0


def setStack(state, index, stack, turn, a, b):
  if state != 0:
    fullfill = state - 8
    if index < 9:
      if stack + 1 == fullfill:
        if (turn - fullfill) % 2 == 0:
          player = "A"
          a = a + fullfill
        else:
          player = "B"
          b = b + fullfill
        print(f"Player {player} scores {fullfill} point(s).")
        return 0, 0, a, b
      else:
        return state, stack + 1, a, b
    else:
      return index, 0, a, b
  else:
    if index > 8:
      return index, 0, a, b
    else:
      return 0, 0, a, b


for i in range(52):
  drew = input()
  index = cards.index(drew)
  if index == -1: exit(f"{drew} is not in cards")
  if drews[index] == 0: exit(f"{drew} drews 4")
  drews[index] -= 1
  remain = 52 - i - 1
  turn = turn + 1
  state, stack, a, b = setStack(state, index, stack, turn, a, b)

print(f"Player A: {a} point(s).")
print(f"Player B: {b} point(s).")
