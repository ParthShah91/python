"""
Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False. 

https://www.interviewkickstart.com/blog/advanced-python-coding-challenges

"""
import collections

def check_duplicate_letters(s):
    """
    Returns true if a word has duplicate letters. Else False
    """
    words = s.split()
    #print("words = ", words)
    has_duplicate = False
    
    for word in words:
        #print("word = ", word)
        res = collections.Counter(word) #Calculate the frequency of letters in the current word
        #print("res = ", res)
        for key in res:
            if res[key] > 1:
                #print(f"*** Duplicate found *** {key} = {res[key]}")
                has_duplicate = True
                break
        if has_duplicate == True: #If the word being currently analysed has duplicates break the main loop
            #print("breaking main loop")
            break

    return has_duplicate
    

if __name__ == "__main__":
    test_str = ["GeeksForGeeks", "", "abcdefgh", "a", "Roses are often red in color"]
    
    for s in test_str:
        print("Test string = ", s)
        ret = check_duplicate_letters(s)
        print("Has_duplicates = ", ret)
        print("\n\n")