# python 2.7
number=input("Δώσε αριθμό")
new=number*3+1
number2=0
while len(str(new))!=1:
    if number2!=0:
        new=new*3+1
    met=len(str(new))
    for i in range(0,met,1):
        number2=number2+int(str(new)[i])
    new=number2
    number2=0
    print new
print "OK"
