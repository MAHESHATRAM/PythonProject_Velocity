def check_anagram(s1,s2):
    if len(s1) == len(s2):
        A1 =sorted(s1)
        A2 = sorted(s2)
        if A1 == A2:
            print(f"Anagram String {A1},{A2}")
        else:
            print("String is Not Anagram")
    else:
        print("String is Not Anagram")
    

word1 = input("Enter string1 to check with another string1:")
word2 = input("Enter string2 to check with another string2:")
check_anagram(word1,word2)