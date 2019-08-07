
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
    
if __name__ == '__main__':    
    # Establishes Dictionaries
    anagrams = {}
    official_anagrams = {}
    
    # Creates anagram out of all of the words longer than eight characters and adds it to Dictionary anagrams
    with open("eng_dict.txt", "r") as file:
        words = file.read().splitlines()
        for word in words:
            if (len(word) >= 8):
                letters = word.lower()
                key = "".join(sorted(letters))
                if key in anagrams:
                    anagrams[key].append(word)
                else:
                    anagrams[key] = [word]

    # Adds anagrams with more than one word to Dictionary official_anagrams
    for key in anagrams:
        if len(anagrams[key]) > 1:
            j = {key : anagrams[key]}
            official_anagrams.update(j)
    print(official_anagrams)