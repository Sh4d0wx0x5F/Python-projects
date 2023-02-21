def plaindrome(word):
    word_2 = word.upper()
    l = len(word) -1
    word_3 = ""
    while l != -1:
        word_3 = word_3 + word_2[l]
        l = l -1
    if word_3 == word_2:
        print("String is a palindrome")
    else:
        print("string is not a palindrome")

word = input(str("Enter a word to check for plaindrome text: "))
plaindrome(word)
