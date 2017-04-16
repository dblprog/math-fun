#!/usr/bin/env python3.3
# vigenere 7 freq -- compute word frequencies from standard input
# SOLUTION SPECIFIC TO 7-char keyword; hard-coded 
# generalized version to come
import sys
import re
import operator

freq1 = {} 
freq2 = {} 
freq3 = {} 
freq4 = {} 
freq5 = {} 
freq6 = {} 
freq7 = {} 

# process input

for line in sys.stdin:

	line = line.rstrip('\n')
	line = line.lower()
	length = len(line)
	length = float(length)/float(7.0)
	c1 = line[0::7]
	c2 = line[1::7]
	c3 = line[2::7]
	c4 = line[3::7]
	c5 = line[4::7]
	c6 = line[5::7]
	c7 = line[6::7]
	for char in c1:
		freq1[char] = freq1.get(char,0) +1
	for char in c2:
		freq2[char] = freq2.get(char,0) +1
	for char in c3:
		freq3[char] = freq3.get(char,0) +1
	for char in c4:
		freq4[char] = freq4.get(char,0) +1
	for char in c5:
		freq5[char] = freq5.get(char,0) +1
	for char in c6:
		freq6[char] = freq6.get(char,0) +1
	for char in c7:
		freq7[char] = freq7.get(char,0) +1

# produce output

from string import ascii_lowercase
print ("\n 1 \n")
for c in freq1.keys():
	print (c, freq1[c]/float(length))
print ("\n 2 \n")
for c in freq2.keys():
	print (c, freq2[c]/float(length))
print ("\n 3 \n")
for c in freq3.keys():
	print (c, freq3[c]/float(length))
print ("\n 4 \n")
for c in freq4.keys():
	print (c, freq4[c]/float(length))
print ("\n 5 \n")
for c in freq5.keys():
	print (c, freq5[c]/float(length))
print ("\n 6 \n")
for c in freq6.keys():
	print (c, freq6[c]/float(length))
print ("\n 7 \n")
for c in freq7.keys():
	print (c, freq7[c]/float(length))

# alphasort = sorted(freq.items(), #sort alphanumerically
# key=operator.itemgetter(0))      
# for word in sorted(alphasort, 
# key=operator.itemgetter(1), 
# reverse=True): 					#sort rest numerically
# 	print("{:<16} {}".format(word[0], word[1]))	


# def letter_freq(file):
# 	freq = {} 
# 	total = 0
# 	for line in file:
# 		for word in re.split("[^a-z]+",line.lower()):
# 			freq[word] = freq.get(word,0) +1
# 			if (word != ''):
# 				total+=1
# 	if '' in freq.keys():
# 		del freq['']
# 	return freq