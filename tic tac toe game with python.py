def pt(a,b,c,d,e,f,g,h,i):
    print(a," | ",b," | ",c)
    print("----------------")
    print(d," | ",e," | ",f)
    print("----------------")
    print(g," | ",h," | ",i)
a="a"
b="b"
c="c"
d="d"
e="e"
f="f"
g="g"
h="h"
i="i"
pt(a,b,c,d,e,f,g,h,i)
q=None
t="X"
print("game will start with X")
z=1
while (z<=9):
    #GAME WILL START WITH X#
    print("X's turn")
    t="X"
    if t=="X" and z<=9:
        x=input("enter block name;") 
        if x=="a":
            a=t
        elif x=="b":
            b=t
        elif x=="c":
            c=t
        elif x=="d":
            d=t
        elif x=="e":
            e=t
        elif x=="f":
            f=t
        elif x=="g":
            g=t
        elif x=="h":
            h=t
        elif x=="i":
            i=t
        pt(a,b,c,d,e,f,g,h,i)
        q=[a==b==c,d==e==f,g==h==i,a==d==g,b==e==h,c==f==i,a==e==i,c==e==g]
        z+=1
        if True in q:
            print ("X is winner")
            break
    print("O's turn")
    t="O"
    if t=="O" and z<9:
        x=input("enter block name;")
        if x=="a":
            a=t
        elif x=="b":
            b=t
        elif x=="c":
            c=t
        elif x=="d":
            d=t
        elif x=="e":
            e=t
        elif x=="f":
            f=t
        elif x=="g":
            g=t
        elif x=="h":
            h=t
        elif x=="i":
            i=t
        pt(a,b,c,d,e,f,g,h,i)
        q=[a==b==c,d==e==f,g==h==i,a==d==g,b==e==h,c==f==i,a==e==i,c==e==g]
        z+=1
        if True in q:
            print("O is winner")
            break
else:
    print("Noone is winner")