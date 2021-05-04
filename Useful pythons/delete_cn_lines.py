s = ''
with open('t.txt') as f:
    for line in f:
        no_cn_chr = True
        for ch in line:
            if ch > '\u00ff':
                no_cn_chr = False
                break
        if no_cn_chr:
            s += line
with open('t.txt', 'w') as f:
    f.write(s)
    print(s)