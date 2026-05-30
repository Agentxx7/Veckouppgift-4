def uppgift1a():
  limit = 15
  index = 5
  
  while index < limit:
      index += 2
      print(index)
        
def uppgift1b():
  for i in range(10):
      if i == 5:
          print("")
      else:
            print(i)
      i = i + 1          

def uppgift1c():
    counter = 0
    for i  in range(6):
        counter += i
        print(counter)

def uppgift1d():
    x = 0
    y = 1
    
    while x < 10:
        if y % 2 ==0:
           x -= y
        else:
            x += y * y
        y += 1
    print(x)

def uppgift1e():
    message = "its_time_to_get_coding"
    print(message[4:8])
    
def uppgift1f():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y + 1:
                s += "#"
            else:
                s += "."
        print(s)