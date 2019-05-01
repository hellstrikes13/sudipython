import random
#this program has proximity of giving duplicate values so indeed we need to shuffle the list and then  slice it 
# but taking the above approach should also result into perfomance if we are setting upperbound to 1 million.
def make_random_ints(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between lower_bound
     and upper_bound. upper_bound is an open bound.
   """
   rng = random.Random()  # Create a random number generator
   result = []
   for i in range(num):
      result.append(rng.randrange(lower_bound, upper_bound))
   return result
a = make_random_ints(5,1,13)
print a
'''
shuffle and slicing
## generate a random object
r = random.Random()
##shuffle the numbers
r.shuffle(numbers)
##slice it
numbers[:5]
'''

