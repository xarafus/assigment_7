def chopping(lst):
if len(lst) >= 2:
  del lst[0]
  del lst[-1]
  return []

def middle(lst):
    if len(lst) >= 3:
        return lst[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4]

print(" my list before calling the chop function ", my_list)
chopping(my_list)
print(" my list after calling the chop function ", my_list)

my_list = [1, 2, 3, 4]

print(" my list before calling the middle function ", my_list)
result = middle(my_list)
print(" my list after calling the middle function ", my_list)

new_list = [1, 2, 3, 4]
print(" new list before calling the middle function ", new_list)
result = middle(new_list)
print(" new list after calling the middle function ", result)
