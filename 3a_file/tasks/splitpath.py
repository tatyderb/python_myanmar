def splitpath(path):
    d, sep, basename = path.rpartition('/')
    if sep:
        d += sep
    file, sep, ext = basename.partition('.')
    if sep:
        ext = sep + ext
    return (d, file, ext)


pathname = input().rstrip()
d, filename, ext = splitpath(pathname)
print('['+d+']')
print('['+filename+']')
print('['+ext+']')