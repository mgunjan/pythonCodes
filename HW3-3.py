import string
import random

'''rev_word method is defined in such a  manner that it will take list of string
as input and return list of reverved words in the fashion requested.The method first
extracts each string from the list and using string properties reverse the string while
keeping in mind the length of the string.
'''
def rev_word(str_list):
    new_list =[]

    for word in str_list:
        wlen= len(word)
        mid= wlen//2
        if mid < 0:
            new_word = word
        if(wlen%2 == 0): #if length of the string is even
            new_word= word[mid:]+word[0:mid]
        else: # reverse for string with odd lengh
            new_word = word[mid+1:]+word[mid]+word[:mid]

        new_list.append(new_word)
    return(new_list)

'''rot13 is simple letter substitution cipher.
rot13 cipher is implemented with the help of translate and maketrans methods
present in string module.First we define the intab which contains the true character
sequence on which rot13 will be applied and outtab defines the cipher value on respective
character sequence. 'maketrans' basically creates the key value pair for intab and respective
outtab and 'translate' makes the changes for each character(key) in the input string by
substituting with value.
'''

def rot13_word(str_list):
    
    intab = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outtab= 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    new_list =[]
    for word in str_list:
        new_list.append(word.translate(word.maketrans(intab, outtab)))
    return(new_list)    

'''
Anagram function operates on each string of the list and randomize the sequence of the characters of
string.
'''
def anagram_word(*args):
     
    str_list=args[0]
    new_list=[]
    for in_str in str_list:
        list1=list(in_str)
        if(len(in_str)<2): # no anagram operation of string with single character. All sentence terminator are in this category.
            out_str= in_str
        elif len(args)==2: # argument has seed value
            xseed = args[1] 
            random.seed(xseed)
            random.shuffle(list1)
            out_str=''.join(list1)
        else:                    # for argument without seed value
            random.shuffle(list1)
            out_str=''.join(list1)
        new_list.append(out_str)    
    return(new_list)    
    



list_str= ['Your', 'oceans', 'are', 'pretty', '.']
print(rev_word(list_str))
print(rot13_word(list_str))
print(anagram_word(list_str))
print(anagram_word(list_str,1010010))


