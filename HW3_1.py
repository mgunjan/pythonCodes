import re  # import regular expression module 

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

    
words= "Hello, world! How are you? Your \noceans are pretty.Incomplete sentence"
print(sep_words(words))
