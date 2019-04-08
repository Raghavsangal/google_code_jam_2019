t=int(input())
for j in range (t):
    n=input()
    # print(n)
    k=str(n)
    k=list(k)
    c=['0']*len(k)
    q=k.count('4')
    if(q==0 or int(n)<4):
        a=n
        b=0
    if(q==1 and int(n)==4):
        a=1
        b=3
    elif(q>=1):
        while(q):
            w=k.index('4')
            k[w]='1'
            c[w]='3'
            q=q-1
        a="".join(k)
        b="".join(c)
        b=b.lstrip('0')
    r=str(j+1)
    print("Case"+" "+"#"+r+":"+" "+str(a)+" "+str(b))