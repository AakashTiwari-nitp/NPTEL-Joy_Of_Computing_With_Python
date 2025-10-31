str = input()

vowelCnt = 0

str = str.lower()
print(str)

for x in str:
    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        vowelCnt += 1

print(vowelCnt)