N,M = map(int, input().split(" "))

#Upper part
for i in range(N//2):
    a = 1+(2*i)
    print(((".|.")*a).center(M,"-"))

#Tag
print ("WELCOME".center(M,"-"))

#lower part
for i in range(N//2):
    a = (N-2)-(2*i)
    print(((".|.")*a).center(M,"-"))
