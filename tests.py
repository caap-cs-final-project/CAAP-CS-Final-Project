
def main():
    with open("eng_dict.txt", "r") as file:
        words = file.read().splitlines()
        anagrams = {}
        for word in words:
            if (len(word) >= 8):
                #word = word.strip("\n")
                letters = word.lower()
                key = "".join(sorted(letters))
                if key in anagrams:
                    anagrams[key].append(word)
                else:
                    #new_list = []
                    #new_list.append(word)
                    #d = {key : new_list}
                    anagrams[key] = [word]
    print(anagrams)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            print("Found some anagrams")
		

				

main()
