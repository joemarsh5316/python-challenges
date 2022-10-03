array = [1, 2, 3, 4, 5]

def print_first_three():
for i in range(3):    
       print(array[i])

def reverse():  
  array.reverse()   
  print(array)

def get_occurrences():  
  char = int(input("Enter a number to add: "))   
 array.append(char)  
  occur = 0 
   for el in array:      
  if el == char:          
  occur += 1  
  print("There are", occur, "occurences of", char)

def remove_index(): 
   index = int(input("Enter a index to remove"))  
  del array[index]  
  print(array)

print_first_three()
reverse()
get_occurrences()
remove_index()

