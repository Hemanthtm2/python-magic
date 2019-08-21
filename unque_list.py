def unique_list(l):
    mylist=[]
    for i in range(len(l)):
        if l[i] in mylist:
            continue
        else:
            mylist.append(l[i])
    return mylist

unique_list([1,2,3,1,1,1])
