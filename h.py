s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
s6=int(input())
total=s1+s2+s3+s4+s5+s6
i=0
per=total//6
print(total,per)
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
        if per>=75:
            print("A+")
        elif per>=60:
            print("A")
        elif per>=50:
            print("B")
        else:
            ("C")
else:
    print("F")
    if s1<35:
            print("fail in s1")
            i=i+1
            if s2<35:
                print("fail in s2")
                i=i+1
                if s3<35:
                        print("fail in s3")
                        i=i+1
                if s4<35:
                        print("fail in s4")
                        i=i+1
                if s5<35:
                        print("fail in s5")
                        i=i+1
                if s6<35:
                        print("fail in s6")
                        i=i+1
                print("no,. of subjects failed =",i)
        

