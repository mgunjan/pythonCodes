def str_insert(dest,ins,position):
    if position < 0 or position > len(dest):
        raise Exception("str_insert(): position input parameter out of range")
        #print("str_insert(): position input parameter out of range")

    #simplest way
    result=dest[0:position]+ins+dest[position:]
    return result

    #alternative method 1

    #dest_l=list(dest)
    #ins_l=list(ins)
    #result_l=dest_l[0:position]+ins_l+dest_l[position:]
    #return str_join(result_l)

    #alternative method 2
    
    #dest_l=list(dest)
    #result_l=dest_l
    #result_l.insert(position,ins)
    #return str_join(result_l)
    
    
def  str_join(list_in,sep=''):
    str_out=''
    for i in list_in[0:-1]:
        str_out=str_out+i+sep
    str_out+=list_in[-1]
    return str_out
