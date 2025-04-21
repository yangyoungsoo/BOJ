T = int(input())

for _ in range(T):
    string = input()

    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')' and '(' in stack:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        print("NO")
    else:
        print("YES")    
            