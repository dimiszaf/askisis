# python 2.7
kakilist=["f","c","k","r","F","C","K","R"]
kalilist=["b","d","g","h","j","l","m","n","p","q","s","t","v","w","x","y","z","B","D","G","H","J","L","M","N","P","Q","S","T","V","W","X","Y","Z"]
f=open("arxio.txt","r")
arxio=f.read()
larxio=arxio.split(" ")
print larxio
for i in range(0,len(larxio),1):
    kakasin=0
    kalasin=0
    fon=0
    for j in range(0,len(larxio[i])):
        if larxio[i][j] in kakilist:
            kakasin=kakasin+1
        elif larxio[i][j] in kalilist:
            kalasin=kalasin+1                    
    if kakasin>kalasin:
        print larxio[i],"= bad word"
    else:
        print larxio[i],"= good word"
f.close        
