import intersting_stuff as yo

bub = yo.anaception()

def check_anaception()
if "acghhhnoooopprrty" in bub:
	print("True BRah!!!")
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

