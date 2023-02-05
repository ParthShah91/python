'''
The program calculates the frequency of words located in a file
Cmd: python word_frequency.py file_name output_file_name
Please note data in output file be overwritten
'''
import sys
import re

if __name__ == "__main__":
    #NPS: Use parseargs or argpaser module
    if len(sys.argv) < 3:
        print("ERR: Please enter file name")
        print("Usage: python word_frequency.py file_name out_file_name")
        print("where,")
        print("file_name - name of file containing words")
        print("out_file_name - output file name where frequency of each word is printed")
        sys.exit(-1)
    
    word_frequency = {}
    #ps: see if try catch block needed
    
    # Open the file. The argument has to be passed as 1st argument
    #NPS: Add Try exception if file does not exist
    with open(sys.argv[1]) as f: #ps: Is it better to have new variable or use this directly?
        for line in f: # Iterate over each line of file
            print("line = ", line)
            words = re.split(' |;|,|\.', line) #ps todo see if more delimiters need to be added
            #NPS: Try using f"words = {words}" new way of print
            print("words = ", words)
            words = list(filter(None, words)) #remove empty strings
            
            for word in words:
                word = word.strip()
                '''
                If word exists in the dictionary increment the count by 1. Else create entry for the word in dictionary
                
                The logic treats uppercase and lowercase words as different strings. Can be modified to treat them as the same word
                '''
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
            print(word_frequency)
            #NPS: no need to add \n It will always print in new line
            print("\n")
        
    with open(sys.argv[2], "w") as f:
        for key in word_frequency:
            f.write(str(key) + ":" + str(word_frequency[key]) + "\n")
         
        
           
        
        
    
    