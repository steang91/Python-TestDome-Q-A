class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word=word.lower() #just setting all characters to lower case for simplicity
        i=len(word)
        for letter in word:
            if letter!=word[i-1]:
                return False
            i=i-1
        return True

print(Palindrome.is_palindrome('Deleveled'))