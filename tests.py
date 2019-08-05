
def main():
	with open("eng_dict.txt", "r") as file:
		anagrams = {}
		for word in file:
			if (len(word) >= 8):
				letters = word
				key = "".join(sorted(letters))
				print(key)
				break

main()
