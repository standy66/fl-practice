import copy
s = raw_input().split()
if len(s) != 2:
    print "Usage: ./main.py regex string"
    exit(1)
reg, u = s
n = len(u)
letters = dict()
for letter in ('a', 'b', 'c'):
    letters[letter] = [{i + 1} if ch == letter else set() for (i, ch) in enumerate(u)]
    letters[letter].append(set())
empty = [{i} for i in range(0, n + 1)]


def check_length(x, k):
    if len(x) <= k:
        print "Incorrect regular expression"
        exit(1)


def multiply_sets(a, b):
    result = [set() for i in range(0, n + 1)]
    for i in range(0, n):
        for end in a[i]:
            result[i] |= b[end]
    return result


x = []
for ch in reg:
    if ch in ('a', 'b', 'c'):
        x.append(letters[ch])
    elif ch == '1':
        x.append(empty)
    elif ch == '+':
        check_length(x, 1)
        a = x.pop()
        b = x.pop()
        x.append([e1 | e2 for (e1, e2) in zip(a, b)])
    elif ch == '.':
        check_length(x, 1)
        a = x.pop()
        b = x.pop()
        x.append(multiply_sets(b, a))
    elif ch == '*':
        check_length(x, 0)
        a = x.pop()
        power = a
        result = copy.deepcopy(empty)
        for k in range(1, n + 1):
            oldResult = copy.deepcopy(result)
            result = [e1 | e2 for (e1, e2) in zip(result, power)]
            if result == oldResult:
                break
            power = multiply_sets(power, a)
        x.append(result)

check_length(x, 0)
ans = x.pop()
x = {i for (i, elem) in enumerate(ans) if n in elem}
print ("INF" if len(x) == 0 else n - min(x))