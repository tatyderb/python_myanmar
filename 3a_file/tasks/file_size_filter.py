def number(x, unit):
    res = float(x)
    res *= 1024
    if unit == 'K':
        return res
    res *= 1024
    if unit == 'M':
        return res
    res *= 1024
    if unit == 'G':
        return res
    print(f'Unknown unit {unit} in size value {x}{unit}')
    return None
        

# filename = 'filesize_short.txt'
filename = 'tmp.txt'
with open(filename) as fin:
    for line in fin:
        a = line.split(maxsplit=9)
        # print(a[0], a[-1])
        size = a[0]
        if size[-1] in '0123456789':
            x = float(size)
        else:
            x = number(size[:-1], size[-1])
        # print(size)   
        if x >= 100*1024:
            print(a[0], a[-1], end='')
                
            
            
            
            
