from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

operator = []
operator += ['+'] * operator_list[0]
operator += ['-'] * operator_list[1]
operator += ['*'] * operator_list[2]
operator += ['/'] * operator_list[3]

def calculate(operators):
    result = num_list[0]
    for i in range(1, N):
        op = operators[i - 1]
        if op == '+':
            result += num_list[i]
        elif op == '-':
            result -= num_list[i]
        elif op == '*':
            result *= num_list[i]
        elif op == '/':
            if result < 0:
                result = -(-result // num_list[i])
            else:
                result = result // num_list[i]
    return result

results = set()
for ops in permutations(operator, len(operator)):
    results.add(calculate(ops))

print(max(results))
print(min(results))
