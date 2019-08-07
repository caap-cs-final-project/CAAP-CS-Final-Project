
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
    
    with open(filename, "r") as file: #opens a file to read
        words = file.read().splitlines() #reads the whole file and splits by line (in the case of the english dictionary, there is only one word per line). Then saves this list of lines to variable names words.
        for word in words: #goes through each word in the list of words
            if (len(word) >= 8): #decides if the word is longer than 8 letters and then continues on with the following statements. If it isn't it ignores it.
                letters = word.lower() #lowercases the word
                key = "".join(sorted(letters)) #creates a "key" which is basically the word with its letters sorted alphabetically
                if key in anagrams: #decides if the key is already in the dictionary. If it is continues with the statements below. If not goes to "else:"
                    anagrams[key].append(word) #adds the 'word' to the key value in the dictionary
                else: #The key was not in the dictionary and it continues on to the following statements
                    anagrams[key] = [word]  #creates a new 'key' in the dictionary with the value of the 'word' attached to it.

    # Adds anagrams with more than one word to Dictionary official_anagrams
    for key in anagrams:
        if len(anagrams[key]) > 1:
            j = {key : anagrams[key]}
            official_anagrams.update(j)
            
    return official_anagrams
    
if __name__ == '__main__':    
    official_anagrams = get_anagrams("eng_dict.txt")
    sorted_keys = sort_keys(official_anagrams)
    #print(official_anagrams)
    #print(sorted_keys)
    for i in range(len(sorted_keys)):
        print(official_anagrams[sorted_keys[i]])
        #pass

