from random import randint
import intersting_stuff as yo
#'abceesu' : ['because', 'pretend this is an anagram of because']
	
	# size of this anagram == 2
	# length of anagram == 7

	# read in the file
	# iterate through the list of words
	# during each iteration
		# check word length
		# sort the letters of the current index
		# check if key exists in dictionary already
			# protip: dictionaries have near-instantaneous lookup time
		# if the key exists
			# add the word to the VALUE associated with that key
		# if the key does not exist
			# create the key value pair

		#

	# value == list of all the words that contain key

	# this_dict = {}
	# this_dict['a_key'] = 'a_value'
	# print(this_dict)
	# print(this_dict['specific_value'])

	# if this_dict['nhvsdjvfucgshjdvzb']:
	# 	# do things
	# else:
	# 	# do other things
    
    
    #######################################################
    #INTERESTING IDEAS:
        #
    #######################################################

def sort_keys(anagrams):
    keys = list(anagrams.keys())
    for i in range(len(keys)):
        smallest = len(anagrams[keys[i]])
        position = i
        for j in range(i+1, len(keys)):
            if len(anagrams[keys[j]]) < smallest:
                smallest = len(anagrams[keys[j]])
                position = j
        if not(position == i):
            keys[i], keys[position] = keys[position], keys[i]
    return keys

def get_anagrams(filename):
    # Creates empty Dictionaries
    anagrams ={}
    official_anagrams = {}
    with open(filename, "r") as file:
        words = file.read().splitlines() 
        for word in words:
            if (len(word) >= 8): 
                letters = word.lower() 
                key = "".join(sorted(letters)) 
                if key in anagrams: 
                    anagrams[key].append(word)
                else:
                    anagrams[key] = [word]  
                    
    # Adds anagrams with more than one word to Dictionary "official_anagrams"
    for key in anagrams:
        if len(anagrams[key]) > 1:
            j = {key : anagrams[key]}
            official_anagrams.update(j)
            
    return official_anagrams
    
if __name__ == '__main__': 
    #starts the program and calls all the functions
    official_anagrams = get_anagrams("eng_dict.txt") 
    sorted_keys = sort_keys(official_anagrams)
    #print(official_anagrams)
    #print(sorted_keys)
    for i in range(len(sorted_keys)):
        print(official_anagrams[sorted_keys[i]])
        #pass

intent = int(input("If you would like to see some interesting anagrams, enter 1. If not, enter 2."))
if  intent == 1:
    which = int(input("Select a function: \n1.) Ananception | 2.) Number_Interesting"))
    if which == 1:
        yo.anaception()
    elif which == 2:
        yo.anumber()
    else:
        print("Goodbye")
else:
    print("Goodbye")

