def hello(name, age):
  return (f"Hello, {name}! You are {age} years old.")
  
response = hello("Brittney", 28)
print(response)

# return will NOT explicitely print anything.
# in my own words, it seems like it returns that value internally
# that way it can be called on in other functions but not displayed until we print()

def add(x, y):
  return x + y

result = add(1, 2)
print(result)