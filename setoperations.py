s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
x=input()
if x=="|":
  print(s1|s2)
elif x=="&":
  print(s1&s2)
elif x=="-":
  print("A-B",s1-s2)
  print("B-A",s2-s1)
elif x=="^":
  print(s1^s2)
elif x==">":
  print(s1>s2)
elif x=="<":
  print(s1<s2)
else:
  print("Incorrect Operation")