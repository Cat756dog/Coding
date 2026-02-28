from Funcs import isPalindrome

while True:
    try:
        pal = isPalindrome(input("Word? "))
    except Exception as e:
        print(f"{e}")
    print(pal.check())