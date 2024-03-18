#idef polindrome():
#    ml = []
#    while True:
#        mstr = input("Enter: ")
#        if mstr.isalpha() and mstr.lower() == "stop":
#            return ml
#        if mstr ==  mstr[::-1]:
#            ml.append(mstr)
#        ml.sort()
#    return ml
#print(polindrome())

#def f(ml):
#    md = {}
#    for i in ml:
#        if type(i) in md:
#            md[type(i)].append(i)
#        else:
#            md[type(i)] = [i]
#    return md
#ml = [123,"Apple",8.99,"A",[1,5,7],{3,9}]
#print(f(ml))


#def f(mstr):
#    sti = 0
#    endi = -1
#    for i in range(len(mstr)//2):
#        if mstr[sti] == mstr[endi]:
#            return mstr[sti]
#        sti += 1
#        endi -= 1
#    return None
#print(f(input("Enter: ")))

#def f(mstr):
#    md = {}
#    ml = []
#    for el in mstr:
#        if el not in md:
#            md[el] = 1
#        else:
#            md[el] += 1
#    for k,v in md.items():
#        if v > 1:
#            ml.append(k)
#    return ml
#print(f(input("Enter: ")))

#def small(ml):
#    small_index = 0
#    for i in range(len(ml)):
#        if ml[i]  < ml[small_index]:
#            small_index = i
#    return small_index
#def selection(ml):
#    nml = []
#    for i in range(len(ml)):
#        sm_ind = small(ml)
#        nml.append(ml.pop(small(ml)))
#    return nml
#ml = [9,2,7,1,0,5]
#print(selection(ml))


