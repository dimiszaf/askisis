# python 2.7
f=open("arxio.txt","r")
keimeno=f.read()
f.close
print keimeno
lista=keimeno.split()
print lista
for i in range(0,len(lista),1):
    if len(lista[i])>3:
        new=lista[i]  
        new=new+new[0]  
        new=new[1:len(new)]        
        new=new+"ay"        
        lista[i]=new
print lista    

