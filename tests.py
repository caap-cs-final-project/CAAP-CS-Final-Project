import intersting_stuff as yo

bub = yo.anaception()

if "acghhhnoooopprrty" in bub:
	print("True BRah!!!")


<<<<<<< HEAD
=======

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
>>>>>>> 29fdc7e31bd2ed4af7e4d4a1a41c863e7446f81a
>>>>>>> d2468684fe26d22a931158304e932781ca611aec
