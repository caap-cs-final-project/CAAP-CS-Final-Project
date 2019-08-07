
def main():
# #Sophia's
#     with open("eng_dict.txt", "r") as file:
#         words = file.read().splitlines()
#         anagrams = {}
#         for word in words:
#             if (len(word) >= 8):
#                 #word = word.strip("\n")
#                 letters = word.lower()
#                 key = "".join(sorted(letters))
#                 if key in anagrams:
#                     anagrams[key].append(word)
#                 else:
#                     #new_list = []
#                     #new_list.append(word)
#                     #d = {key : new_list}
#                     anagrams[key] = [word]
# #    print(anagrams)
# #    for key in anagrams:
# #        if len(anagrams[key]) > 1:
# #            print("Found some anagrams")
# #Branson's
# 	with open("eng_dict.txt", "r") as file:
# 		anagrams = {}
# 		anagrams_final = {}
# 		for word in file:
# 			if (len(word) >= 8):
# 				word = word.strip("\n")
# 				letters = word.lower()
# 				key = "".join(sorted(letters))
# 				if key in anagrams:
# 					anagrams[key].append(word)
# 				else:
# 					new_list = []
# 					new_list.append(word)
# 					d = {key : new_list}
# 					anagrams.update(d)
# 		for list_ans in anagrams:
# 			if len(anagrams[list_ans]) > 1:
# 				j = {list_ans : anagrams[list_ans]}
# 				anagrams_final.update(j)

# 		print(anagrams_final)

#Ismail's
	anagrams = {
		'eirsst' : ['sister', 'resist'],
		'aenprt' : ['parent', 'entrap', 'trepan'],
		'eelssv' : ['selves', 'vessel']
	}

	for key in anagrams.values():
		print(len(key))

				

main()
