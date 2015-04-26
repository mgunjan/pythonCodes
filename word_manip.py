import re  # import regular expression module 
import string
import random
#-----------------------------------------------------------------------------------------------------------
''''sep_words is function which takes a string and returns a list of lists
containing sentences parsed out into word'''

def sep_words(in_str):

    ind =re.finditer('[.!?]',in_str) # returns object which contains location of sentence terminators.
    loc = []
    for match in ind:
       tup=match.span()
       loc.append(tup[1])
       
    if loc[-1] != len(in_str): 
       loc.append(len(in_str))
    
    str_list=[]
    #print(loc)
    first=0
    last =0
    for ind in loc:
       last= ind
       str_list.append(in_str[first:last])
       first = last    
    #print(str_list)
    word_list=[]
    for word in str_list:
       ##word_list.append(word.split())
       if word[-1]== '!' or word[-1]== '?' or word[-1]== '.':
          word = word[:-1]+' '+word[-1]
       word_list.append(word.split())   
          
       #print(word_list)
    return(word_list)
#----------------------------------------------------------------------------------------------------------

def comb_words(list_str):
    list2=[]
    for item in list_str:
        list1= ' '.join(item)
        if(list1[-1]=='!' or list1[-1]=='.' or list1[-1]=='?'):
            list1 =list1[:-2]+list1[-1]
        list2.append(list1)

    comb_str=' '.join(list2)
    return(comb_str)

#--------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------
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
    
#----------------------------------------------------------------------------------------------------------------------------------
