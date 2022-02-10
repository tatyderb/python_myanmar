def splitpath(path):
    d, sep, basename = path.rpartition('/')
    if sep:
        d += sep
    file, sep, ext = basename.partition('.')
    if sep:
        ext = sep + ext
    return (d, file, ext)

filename = 'filelist.txt'
count = 0
with open(filename) as fin:
    for line in fin:
        d, filename, ext = splitpath(line.strip())
        if filename.startswith('task') and ext == '.py':
            count += 1
            
print(count)
