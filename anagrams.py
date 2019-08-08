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
    #sorts the dictionary keys by length of their values
    #if you want the sorted dictionary you should refrence the sorted keys list
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

def sort_segment(keys):
    #sorts the dictionary keys by length of their values
    #if you want the sorted dictionary you should refrence the sorted keys list
    for i in range(len(keys)):
        smallest = len(keys[i])
        position = i
        for j in range(i+1, len(keys)):
            if len(keys[j]) < smallest:
                smallest = len(keys[j])
                position = j
        if not(position == i):
            keys[i], keys[position] = keys[position], keys[i]
    return keys

def sort_wordlength(sorted_keys,anagrams):
    #this function sorts the anagrams within the same size by length
    curr_size = len(anagrams[sorted_keys[0]])
    start = 0
    end = 1
    for i in range(len(sorted_keys)):
        if curr_size != len(anagrams[sorted_keys[i]]):
            sorted_keys[start:end] = sort_segment(sorted_keys[start:end])
            start = i
            end = i+1
            curr_size = len(anagrams[sorted_keys[i]])
        else:
            end += 1
    return sorted_keys



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

def cool_stuff():
    intent = int(input("If you would like to see some interesting anagrams, enter 1. If not, Type Any other number to exit.\nInput: "))
    if  intent == 1:
        which = int(input("Select a function: \n1.) Ananception | 2.) Number_Interesting \nType Any other number to exit.\nInput: "))
        if which == 1:
            yo.anaception()
        elif which == 2:
            yo.anumber()
        else:
            exit("\nGoodbye!")
    else:
        exit("\nGoodbye!")
    return

        
if __name__ == '__main__': 
    #starts the program and calls all the functions
    print("\t\t\t\tANAGRAMS from the English Dictionary!!")
    print("\n")
    official_anagrams = get_anagrams("eng_dict.txt") 
    sorted_keys = sort_keys(official_anagrams)
    sortedkeys_by_wordlengths = sort_wordlength(sorted_keys, official_anagrams)
    try:
        format = int(input("Would you like to view them line by line, or all together?\n{1} Line by Line\n{2} All together\n{Any other number} Exit Program\nInput: "))
    except:
        print("Please enter a number!")
    if format == 1:
        for i in range(len(sorted_keys)):
            print("ANAGRAM LETTERS:",sortedkeys_by_wordlengths[i], " -> WORDS:", official_anagrams[sortedkeys_by_wordlengths[i]])
            pass
    elif format == 2:
        for i in range(len(sorted_keys)): 
            print("ANAGRAM LETTERS:",sortedkeys_by_wordlengths[i], " -> WORDS:", official_anagrams[sortedkeys_by_wordlengths[i]], "\t...........\t", end ='')
            # print('Length of list: ', len(official_anagrams[sortedkeys_by_wordlengths[i]]), end=' ')
            # print('Length of key: ', len(sortedkeys_by_wordlengths[i]))
            pass
    else:
        exit("\nGOODBYE!")
    print("\n\n")
    cool_stuff()
    print("GOODBYE!")
 


