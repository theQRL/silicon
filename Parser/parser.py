import pandas as pd

#  TODO: 
#     1> Refactoring 
#     2> Reduce time complexity by replacing recursion by dynamic programming

filename = "grammar"
with open(filename, "r") as f:
    data = f.read().strip()

result = []
left = set()
right = dict()

sym = ''

i = 0
last = None
while i < len(data):
    c = data[i]

    if c == '|':
        right[last].add(sym.strip())
        #right[-1].append(sym.strip())
        sym = ''

    elif c == '\n':
        sym = sym.strip()
        if len(sym) > 0:
            right[last].add(sym)
            sym = ''

    elif c == '-' and i + 1 < len(data) and data[i + 1] == '>':
        last = sym.strip()
        left.add(last)
        right[last] = set()
        sym = ''
        i += 1

    elif c == '@':  # Terminator
        sym = sym.strip()
        if len(sym) != 0:
            raise Exception("Invalid Grammar")
        right[last].add(c)
    else:
        sym += c

    i += 1

sym = sym.strip()
if len(sym) > 0:
    right[last].add(sym)

for k, v in right.items():
    print(k, '\t', v)


# TABLE
headers = set()
for key in right:
    for item in right[key]:
        syms = item.split(' ')
        for sym in syms:
            sym = sym.strip()
            if sym not in left:
                headers.add(sym)
print('------')
print(headers)

def first(key):
    global left, right
    ans = set()
    for value in right[key]:
        v = value.split(' ')[0]
        if v == '@':
            ans.add('@')
        elif v in left:
            if v == key:
                continue
            new_ans = first(v)
            ans = ans.union(a for a in new_ans)
        else:
            ans.add(v)
    return ans

def follow(key, ans):
    ans[key] = set()
    for k in right:
        for v in right[k]:
            syms = v.split(' ')
            i = -1

            while i < len(syms) - 1:
                i += 1
                sym = syms[i]

                if sym != key:
                    continue

                if i + 1 < len(syms):
                    global first_dict
                    if syms[i+1] in first_dict:
                        f = first_dict[syms[i+1]]
                    else:
                        f = {syms[i+1]}
                    if '@' in f:
                        if key == k:
                            continue
                        if ans[k]:
                            temp = ans[k]
                        else:
                            ans = follow(k, ans)
                            temp = ans[k]
                        ans[key] = ans[key].union(temp)
                        ans[key] = ans[key].union(f) - {'@'}
                    else:
                        ans[key] = ans[key].union(f)
                else:
                    if key == k:
                        continue
                    if ans[k]:
                        temp = ans[k]
                    else:
                        ans = follow(k, ans)
                        temp = ans[k]
                    ans[key] = ans[key].union(temp)
    return ans

first_dict = dict()  # Keeps track of first

for key in left:
    first_dict[key] = first(key)

print("** First **"*10)

for k, v in first_dict.items():
    print(k, v)

# FOLLOW

follow_dict = dict()

for key in left:
    follow_dict[key] = None

for key in left:
    follow_dict = follow(key, follow_dict)

print('** Follow **'*10)

for k in follow_dict:
    if len(follow_dict[k]) == 0:
        follow_dict[k] = {'$'}

for k, v in follow_dict.items():
    print(k, v)


# LL1 PARSER

def ll1():
    global first_dict, right, follow_dict
    table = {}
    for k in right:
        for v in right[k]:
            syms = v.split(' ')
            sym = syms[0]
            if sym == k:
                continue
            if sym != '@':
                if sym in first_dict:
                    f = first_dict[sym] - {'@'}
                else:
                    f = [sym]
                for e in f:
                    print('--> ', k, e, v)
                    table[k, e] = v
            else:
                for e in follow_dict[k]:
                    print('==> ', k, e, v)
                    table[k, e] = v

    for k, v in table.items():
        print(k, "=>", v)

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]

    print("\n")
    print(pd.DataFrame(new_table))
    print("\n")

    return table


ll1()


