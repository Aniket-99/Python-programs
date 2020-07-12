#a = ['aniket','@larma','ii','@sd','@sghj']
a = input("Enter a sentence").split(' ')



for val in a:
    if '@' in val[0]:
        print(val[1])

