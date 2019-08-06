
def main():
	with open("eng_dict.txt", "r") as file:
		anagrams = {}
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

		print(anagrams)
		

				

main()
