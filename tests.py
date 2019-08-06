
def main():
	with open("eng_dict.txt", "r") as file:
		anagrams = {}
		anagrams_final = {}
		for word in file:
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

		print(anagrams_final)
		

				

main()
