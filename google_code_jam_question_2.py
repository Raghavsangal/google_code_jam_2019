t=int(input())
for k in range (t):
    n=int(input())
    s=input()
    s=list(s)
    a=''
    for i in range(len(s)):
        if(s[i]=='S'):
            a+='E'
        if(s[i]=='E'):
            a+='S'
    r=k+1
    print("Case"+" "+"#"+str(r)+":"+" "+a)