def is_increasing(lst):
      #Base case
  if not lst:
    return None
  #Recursion
  elif len(lst) != 2 and lst[0] < lst[1]:
    return is_increasing(lst[1:])
  elif len(lst) == 2 and lst[0] < lst[1]:
    return True
  else: 
    return False
