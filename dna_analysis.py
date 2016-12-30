def is_valid(base):
    return base in ['A', 'G', 'T', 'C']

def gc_content(gc, total):
    for i in list:
       if i in ['G', 'C']:
         # print "fdafafaf"
          gc += 1
    total = len(list)     
    return gc


index = 0           # Define the list initial index
gc = 0              # Define the initial number index of gc
total = 0           # Define the initial number index of total bases
list = []           # Define an empty list

print ("Enter your sequence one base at a time. ")
while True:
    #gc = 0
    base = raw_input()
    if  is_valid(base) == 1:
        list.insert(index, base)
        index += 1
        #gc_content(gc, total)
        print "GC: ", gc_content(gc, total)
    else:
        #gc_content(gc, total)
        if  base == '': 
            print ("DNA Sequence: "), ''.join(list)
            print len(list)
            print gc_content(gc, total) 
            print "GC Content: ", (gc_content(gc, total)*100/len(list)), "%"
            exit()        
        else:
            print "GC: ", gc_content(gc, total)
    
