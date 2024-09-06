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
l=[]
l2=["a","b","c","d","e","f","g","h","i"]
print("game will start with X")
z=1
while (z<=9):
    #GAME WILL START WITH X#
    print("X's turn")
    if t=="X" and z<=9:
        x=input("enter block name;") 
        if x in l:
            print("NO CHEATING")
            t="X"
            continue
        elif x not in l2:
           print ("enter valid place")
           t="X"
           continue
        else:
            if x=="a":
               a=t
               l.append("a")
               t="O"
            elif x=="b":
               b=t
               l.append("b")
               t="O"
            elif x=="c":
              c=t
              l.append("c")
              t="O"            
            elif x=="d":
               d=t
               l.append("d")
               t="O"
            elif x=="e":
              e=t
              l.append("e")
              t="O"
            elif x=="f":
              f=t
              l.append("f")
              t="O"
            elif x=="g":
              g=t
              l.append("g")
              t="O"
            elif x=="h":
              h=t
              l.append("h")
              t="O"
            elif x=="i":
              i=t
              l.append("i")
              t="O"
            pt(a,b,c,d,e,f,g,h,i)
            q=[a==b==c,d==e==f,g==h==i,a==d==g,b==e==h,c==f==i,a==e==i,c==e==g]
            z+=1
            if True in q:
              print ("X is winner")
              break
            else:
               print("Os turn")
    if t=="O" and z<9:
        x=input("enter block name;")
        if x in l:
            print("NO CHEATING")
            t="O"
            continue
        elif x not in l2:
           print("Enter valid place")
           t="O"
           continue
        else:
            if x=="a":
               a=t
               l.append("a")
               t="X"
            elif x=="b":
               b=t
               l.append("b")
               t="X"
            elif x=="c":
              c=t
              l.append("c") 
              t="X"             
            elif x=="d":
               d=t
               l.append("d")
               t="X"
            elif x=="e":
              e=t
              l.append("e")
              t="X"
            elif x=="f":
              f=t
              l.append("f")
              t="X"
            elif x=="g":
              g=t
              l.append("g")
              t="X"
            elif x=="h":
              h=t
              l.append("h")
              t="X"
            elif x=="i":
              i=t
              l.append("i")
              t="X"
            pt(a,b,c,d,e,f,g,h,i)
            q=[a==b==c,d==e==f,g==h==i,a==d==g,b==e==h,c==f==i,a==e==i,c==e==g]
            z+=1
            t="X"
            if True in q:
              print ("X is winner")
              break
else:
    print("Noone is winner")
