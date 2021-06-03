# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:46:17 2018

@author: Lucas Deutschmann
"""

from math import sqrt

# Input: Anagramic word pair w1, w2 and an integer n1
# Output: Rearranged integer n2 based on the permutation from w1 to w2         
def CalculatePermutation(w1, w2, n1):
    
    # Get object representation of number
    n1_repr = repr(n1)
    
    # Get word lenght
    w_len = len(w1)
    
    # Check for equal sizes
    if (w_len != len(w2)) or (w_len != len(n1_repr)):
        return 0

    # Build dictionary
    dic = {}
    for i in range(w_len):
        # Check if key is already mapped to a different value
        if (w1[i] in dic) and (dic[w1[i]] != n1_repr[i]):
            return 0
        # Ensure every digit is only assigned once
        if (n1_repr[i] in dic.values()) and not (w1[i] in dic):
            return 0
        dic[w1[i]] = n1_repr[i]

    # Determine and return n2
    n2_repr = ''
    for i in range(w_len):
        n2_repr += dic[w2[i]]
    n2 = (int)(n2_repr)
    return n2


# Read file
words_file = open('p098_words.txt', 'r')
words = words_file.read()
words_file.close()

# Convert string to List of strings
words = words[1:len(words)-1].split('","')

# Sort words by number of letters
word_lists = []
for i in range(len(max(words,key=len))):
    word_lists.append([])
for word in words:
    word_lists[len(word)-1].append(word)

# Find word pairs
word_pairs = []
for word_list in word_lists:
    for i in range(0, len(word_list)):
        for j in range(i+1, len(word_list)):
            if (''.join(sorted(word_list[i])) == ''.join(sorted(word_list[j]))):
                word_pairs.append((word_list[i], word_list[j]))
    
# Iterate through pairs, starting with the longest words
result = 0
w_len = 0
for word_pair in word_pairs[::-1]:
    
    # Check if solution was found for greater numbers already
    if (w_len != len(word_pair[0])) and (result > 0):
        break
        
    # Setup
    w_len = len(word_pair[0])
    i_start = (int)(sqrt(10**(w_len-1)))+1
    sq = i_start ** 2
    sq_inc = 2 * i_start + 1
    sq_end = 10**w_len
    
    # Iterate over all squares
    while (sq < sq_end):
        
        # Get rearranged number
        n2 = CalculatePermutation(word_pair[0], word_pair[1], sq)
        
        # Check if rearranged number is a square
        if (n2 != 0) and (sqrt(n2).is_integer()) and (w_len == len(repr(n2))):
            if (sq > result):
                result = sq
            if (n2 > result):
                result = n2
        
        # Calculate next square
        sq += sq_inc
        sq_inc += 2
    
# Print result
print(result)

"""
All Anagramic Squares
(w1, w2, sq1, sq2) 
DOG GOD 169 961
DOG GOD 961 169
EAT TEA 256 625
EAT TEA 961 196
HOW WHO 256 625
HOW WHO 961 196
ITS SIT 256 625
ITS SIT 961 196
NOW OWN 196 961
NOW OWN 625 256
CARE RACE 1296 9216
CARE RACE 9216 1296
DEAL LEAD 1764 4761
DEAL LEAD 4761 1764
EAST SEAT 2916 1296
FILE LIFE 1296 9216
FILE LIFE 9216 1296
HATE HEAT 1369 1936
MALE MEAL 1369 1936
MEAN NAME 2401 1024
MEAN NAME 9604 4096
NOTE TONE 1296 9216
NOTE TONE 9216 1296
POST SPOT 2916 1296
POST STOP 1024 2401
POST STOP 4096 9604
RATE TEAR 1024 2401
RATE TEAR 4096 9604
SHUT THUS 1764 4761
SHUT THUS 4761 1764
BOARD BROAD 17689 18769
"""
