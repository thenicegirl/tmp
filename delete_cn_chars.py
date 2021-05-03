s = ''
with open('t.txt') as f:
    for line in f:
        for ch in line:
            if ch < '\u00ff':
                s += ch
with open('t.txt', 'w') as f:
    f.write(s)
    print(s)