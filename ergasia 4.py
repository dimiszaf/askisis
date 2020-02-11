# python 2.7
def asci(lexi):
    sume=""
    for i in range(0,len(lexi),1):
        sume=sume+str(ord(lexi[i]))
        print sume
    met=0   
    for j in range(1,int(sume)+1,1):
        if int(sume)%j==0:
            met=met+1
        if met>2:
            break
    if met>2:
        print "O",sume ,"Δεν είναι πρώτος"
    else:
        print "O",sume ,"είναι πρώτος"
x=raw_input("...")
asci(x)

    
