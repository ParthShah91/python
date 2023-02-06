'''
The program calculates the frequency of words located in a file
Cmd: python word_frequency.py file_name output_file_name
Please note data in output file be overwritten
'''
import sys
import re
import argparse

if __name__ == "__main__":
    #NPS: Use parseargs or argpaser module
    input_fname = ''
    output_fname = '' 
    parser = argparse.ArgumentParser(description='Calculate frequency of words in a file')
    parser.add_argument('-i', '--input', help='File containing text to measure frequency of words', required=True)
    parser.add_argument('-o', '--output', help='Output file displaying frequency of words in the input file', required=True)
    args = parser.parse_args()  
    
    print(f"args = {args}")
    print(args.input)
    print(args.output)
    
    word_frequency = {}
       
    # Open the file. The argument has to be passed as 1st argument
    #NPS: Add Try exception if file does not exist
    try:
        with open(args.input) as f: #ps: Is it better to have new variable or use this directly?
            for line in f: # Iterate over each line of file
                print(f"line = {line}")
                words = re.split(' |;|,|\.', line) #ps todo see if more delimiters need to be added
                #NPS: Try using f"words = {words}" new way of print
                print(f"words = {words}")
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
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
    else:
        with open(args.output, "w") as f:
            for key in word_frequency:
                f.write(str(key) + ":" + str(word_frequency[key]) + "\n")
         
        
           
        
        
    
    