a = input("Enter a word to check wheather the word is palidrom or not")
l= len(a)
for i in range((len(a)//2)):
    if a[i] == a[-(i+1)]:
        print(a, " " ",""Not a palindrom")
        break
else:
    print("String is a palindrom")