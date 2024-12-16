def calculate(expr):
  stack = []
  tokens = expr.split()

  for token in tokens:
    if token.isdigit():
      stack.append(int(token))
    elif token in "+-*/":
      try:
        val2 = stack.pop()
        val1 = stack.pop()
        if token == "+":
          result = val1 + val2
        elif token == "-":
          result = val1 - val2
        elif token == "/":
          result = val1 / val2
        elif token == "*":
          result = val1 * val2
        else:
           return "Error!"
        stack.append(result)
      except:
        return "Error!"
    else:
        return "Error!"

  if len(stack) != 1:
    return "Error!"

  return stack[0]

expression = "2 3 - 12 10 - * 4 2 / +"

print(f"Answer: {calculate(expression)}")
