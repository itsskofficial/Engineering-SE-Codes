def longest_word(sentence):
    words=sentence.split(" ")
    words_length=[len(i) for i in words]
    return words[words_length.index(max(words_length))]

def frequency(sentence,character):
    frequency_list=[i for i in sentence if i==character]
    return len(frequency_list)

def palindrome(sentence):
    if sentence==sentence[::-1]:
        print ("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

def substring(sentence,sub):
    if sub in sentence:
        return (sentence.index(sub))

def count(sentence,word):
    words_list=sentence.split(" ")
    word_count=0
    for i in words_list:
        if i == word:
            word_count+=1
    return word_count

sentence=input("Enter a sentence: ")

longestWord=longest_word(sentence)
print(f"The longest word in the sentence is: {longestWord}")

character=input("Enter character that you want the frequency of: ")
frequent=frequency(sentence,character)
print(f"The character appears {frequent} times")
palindrome(sentence)

sub=input("Enter substring you want to find: ")
sub_index=substring(sentence,sub)
print(sub_index)

word=input("Enter the word you want to find: ")
word_count=count(sentence,word)
print(word_count)