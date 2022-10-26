
import re
   #built in library with regular expressions

# fuck_off ='Two words, FUCK! easy to understand. OFF! very easy to understand. FUCK OFF!!'  #string of words

# matches = re.findall("FUCK", fuck_off)  #variable storing the "re" library with .findall function that looks for a match 
# matches_case = re.findall("fuck", fuck_off, re.IGNORECASE) #IGNORECASE ignores the case of the words and returns if matched

# print(matches)
# print(matches_case)




# zen = """Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""

# m = re.findall("^If", zen, re.MULTILINE) #findall functions looks with in the string to try and match what is in the parameter. 
#                         #multiline is used to look for matches on all of the lines of a multiline screen.
# print(m)

###finding multiple character in a string 
# str = "Two too"

# m = re.findall("t[wo]o", str, re.IGNORECASE) #regular expression matches  “t” followed by either [w or o] followed by a “o”

# print (m)
###finding digits in a string 

# str = "123 hi 456"

# m = re.findall("\d", str, re.IGNORECASE)

# print (m)

###repetition 

# t = "_one_ _two_ _three_"

# greedy = re.findall("_.*_", t,) #greedy version, looks for all matches with between underscored, including them. return together
# non_greedy = re.findall("_.*?_", t) #non greedy version looks for individual matches

# # for match in greedy:
# #    print(greedy)

# for match in non_greedy:
#    print (non_greedy)
#    break #break is used to you dont get multiple prints. after the loop iterates once, it breaks.


# str = "Arizona 479, 501, 870. California 209, 213, 650."

# m = re.findall("\d", str)

# print (m)

# str = "The ghost that says boo haunts the loo."

# # m = re.findall(".oo", str) #special charactet '.' matches the oo

# print(m)
