import string
import re

def find_mirrors(in_file, out_file):
 # list for holding in_file items
    lines = []

# Function to check whether the input word in in_file is palindrome or not
def is_palindrom(word):
    word = ''.join(c.lower() for c in word if c not in string.punctuation)
# For making a case sensitive compare    
# --   word != re.search('Ababa', 'ababA',re.IGNORECASE) ---
    if word == word[::-1]:
       return True
        
    return False
    
# open in_file in read mode    
with open('linuxwords.txt', 'r') as in_file:
 
# Reading in_file content line by line and storing in 'words' list after 
#ignoring white spaces,\t,\r etc chars in_file using .strip()
        lines = in_file.readlines()
        words = [line.strip() for line in lines]
       
# list for holding non-palindrome words 
to_write = []

#initializing count
cnt = 0
# checking whether the input word in the 'words' list be a palindrome or not
for word in words:
	if not is_palindrom(word) :
		# Appending non-palindrome words to 'to_write' list 
		to_write.append(word[::-1])
	else:
		cnt += 1
		
# printing palindrome count		
print('there are ' + str(cnt) + ' palindromes!')
	
# open out_file for write mode	
with open('output.txt', 'w') as out_file:   

# Iterating through 'to_write' list that has non-palindromes
      for word in to_write[:-1]:

# writing non-palindrome(original) word followed by '/' followed by reversed word 
 #till the end of the 'to_write' list to out_file     
      	out_file.write(word[::-1] + '/' + word + '\n')
      out_file.write(to_write[-1])