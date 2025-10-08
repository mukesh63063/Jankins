class Calculator:
  def __init__(self, a, b):
    a.self = a
    b.self = b
def add(self):
  return a.self+b.self
def sub(self):
  return a.self-b.self

c = Calculator(20, 10)
print(c.add)
print(c.sub)
