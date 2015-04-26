
def comb_words(list_str):
    list2=[]
    for item in list_str:
        list1= ' '.join(item)
        if(list1[-1]=='!' or list1[-1]=='.' or list1[-1]=='?'):
            list1 =list1[:-2]+list1[-1]
        list2.append(list1)

    comb_str=' '.join(list2)
    return(comb_str)



list_str=[['Hello,', 'world', '!'], ['How', 'are', 'you', '?'], ['Your', 'oceans', 'are', 'pretty', '.'], ['Incomplete', 'sentence']]     
print(comb_words(list_str))




