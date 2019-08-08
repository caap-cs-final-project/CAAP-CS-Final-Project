
anagrams = {}
anagrams_final = {}
word_list = []

#testing main function
def main():
    print("\t\t\t\tANAGRAMS from the English Dictionary!!")
    print("\n")
    official_anagrams = {'key1' : [0,1,2], 'key2' : [1,2,3], 'key3' : [3,2,1]}
    sorted_keys = ['key1', 'key2', 'key3']
    try:
        format = int(input("Would you like to view them line by line, or all together?\n{1} Line by Line\n{2} All together\n{Any other number} Exit Program\nInput: "))
    except:
        print("Please enter a number!")
    if format == 1:
        for i in range(len(sorted_keys)):
            print("ANAGRAM LETTERS:",sorted_keys[i], " -> WORDS:", official_anagrams[sorted_keys[i]])
            pass
    elif format == 2:
        for i in range(len(sorted_keys)): 
            print("ANAGRAM LETTERS:",sorted_keys[i], " -> WORDS:", official_anagrams[sorted_keys[i]], "\t...........\t", end ='')
            # print('Length of list: ', len(official_anagrams[sortedkeys_by_wordlengths[i]]), end=' ')
            # print('Length of key: ', len(sortedkeys_by_wordlengths[i]))
            pass
    else:
        exit("\nGOODBYE!")
    print("\n\n")
    print("calling another function")
    print("GOODBYE!")
main()
 
def __init__():
	with open("eng_dict.txt", "r") as file:
			global anagrams
			global anagrams_final
			global word_list 
			for word in file:
				word = word.strip("\n")
				word_list.append(word)
				if (len(word) >= 8):
					word = word.strip("\n")
					letters = word.lower()
					key = "".join(sorted(letters))
					if key in anagrams:
						anagrams[key].append(word)
					else:
						new_list = []
						new_list.append(word)
						d = {key : new_list}
						anagrams.update(d)
			for list_ans in anagrams:
				if len(anagrams[list_ans]) > 1:
					j = {list_ans : anagrams[list_ans]}
					anagrams_final.update(j)



__init__()

# def anagram_word():
# 	global anagrams_final
# 	global word_list
# 	for keys in anagrams_final:
# 		if keys in anagrams:
# 			print(anagrams_final[keys])
# anagram_word()
		#print(anagrams_final)



def anaception():
	with open("eng_dict.txt", "r") as file:
		limit = int(input("Enter the Smallest length of contained word. \n Enter Here> "))
		words_or = int(input("If you would like to find words, enter 1. If you would like to find anagrams, enter 2.\n Enter Here> "))
		all_words = {}
		for word in file:
			word = word.strip("\n")
			letters = word.lower()
			key = "".join(sorted(letters))
			d = {key : word}
			all_words.update(d)
		impress = []
		interst = False
		anagrams_cool = {}
		for keys in anagrams_final:
			for num in range(len(keys)):
				k=0
				while (k+num < len(keys)) and limit<=num:
					if(words_or == 1 ):
						if (keys[k:k+num] in all_words) and (all_words[keys[k:k+num]] not in impress):    #if you replace all_words with anagrams_final, only anagrams can be contained
							if keys not in anagrams_cool:
								d = {keys : anagrams_final[keys]}
								anagrams_cool.update(d)
								# print("******** ANAGRAMS_COOL! ********")
								# print(anagrams_cool)
							interst = True
							impress.append(all_words[keys[k:k+num]])
							# print("********************* Here we go! ******************")
							# print(impress)
							k+=1
						else:
							k+=1
					else:
						if (keys[k:k+num] in anagrams_final) and (keys[k:k+num] not in impress):    #if you replace all_words with anagrams_final, only anagrams can be contained
							if keys not in anagrams_cool:
								d = {keys : anagrams_final[keys]}
								anagrams_cool.update(d)
								# print("******** ANAGRAMS_COOL! ********")
								# print(anagrams_cool)
							interst = True
							impress.append(keys[k:k+num])
							# print("********************* Here we go! ******************")
							# print(impress)
							k+=1
						else:
							k+=1
		if(interst):
			print("\n**** Here are the hashes/words ****\n")
			print(impress)
			print("\n**** Here are the interesting Angagrams ****\n")
			print(anagrams_cool)

anaception()

def sort_keys():
    anagrams = {
        'eilnst' : ['enlist', 'listen', 'silent'],
        'aenprt' : ['parent', 'entrap']
    }
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
sort_keys()

def sort_segment():
    anagrams = {
        'eilnst' : ['enlist', 'listen', 'silent'],
        'aenprt' : ['parent', 'entrap']
    }
    keys = list(anagrams.keys())
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
sort_segment()

def sort_wordlength(sorted_keys,anagrams):
    anagrams = {
        'eilnst' : ['enlist', 'listen', 'silent'],
        'aenprt' : ['parent', 'entrap']
    }
    sorted_keys = {
    	'aenprt' : ['parent', 'entrap'],
    	'eilnst' : ['enlist', 'listen', 'silent']
    }
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
sort_wordlength()
