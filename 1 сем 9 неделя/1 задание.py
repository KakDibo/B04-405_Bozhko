def convert(expression):
  ops = {"+": 1, "-": 1, "*": 2, "/": 2}
  stk = []
  res = []

  for tok in expression.split():
    if tok.isdigit():
      res.append(tok)
    elif tok in ops:
      while stk and ops.get(stk[-1], 0) >= ops[tok]:
        res.append(stk.pop())
      stk.append(tok)
    elif tok == "(":
      stk.append(tok)
    elif tok == ")":
      while stk and stk[-1] != "(":
        res.append(stk.pop())
      stk.pop()

  while stk:
    res.append(stk.pop())

  return " ".join(res)

expr = "( 2 - 3 ) * ( 12 - 10 ) + 4 / 2"

print(f"RPN: {convert(expr)}")