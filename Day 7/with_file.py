with open("demo.txt","r") as f:
  data=f.read()
  print(data)
  f.close() # Not necessary in with syntax

with open("demo.txt","w") as f:
  f.write("Orchid international college")
  