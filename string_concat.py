
def str_join(s_list,sep=''):
    out_list=''
    out_list1=''
    sep_len= len(sep)
    if(sep_len==0):
        for elem in s_list:
            out_list+=elem
    else:
        for elem in s_list:
            out_list1 += (elem + sep)
        out_list=out_list1[:-sep_len]
    return out_list
    
slist=['apple','banana','pear']
sep = '>>>'
print(str_join(slist,sep))

