#!/usr/bin/env python3

import sys
import re

# returns y s.t. xy = b mod n
def mod_division(x,b,n):
  for val in range(1,n):
    if ((x*val)%n) ==b:
      return val
  return -1 # failure 
    
# creates appropriate permutation if possible, else returns None               

def find_perm(n): 

  permute = [0,1]
  attained = [0,1]
  
  for k in range(2,n):
    permute.append(0)
    attained.append(0)

  for i in range(2,n):
    # Such permutations only exist for prime n; bail if composite (divisible by some i < n)
      if n%i == 0:
        return None;
    # else = i mod n                                      
      j = mod_division(i-1,i,n)

      if attained[j] == 1:
        return None;

      permute[i] = j
      attained[j] = 1
  return permute;

def array_factorial(lst):
  s = 1
  for i in re.split('\*', lst):
      s*=int(i) 
  return s

for arg in range(1,len(sys.argv)):
  n = int(sys.argv[arg]);
  perm = find_perm(n);
  if perm is None:
    print("Impossible to find such a permutation for n= " + str(n))
  else:
    print("A permutation is possible for n = "+str(n)+":")
    for num in range(1,n):
      s = ""
      for i in range(1,num):
        s += str(perm[i]) + "*"

      s += str(perm[num])
      
      print( str(s) + "(=" +  str(array_factorial(s)) +") = " + str(num) + " mod ("  + str(n) + "); ", end="")
      print()


