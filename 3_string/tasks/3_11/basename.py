def basename(path):
    dirname, sep, filename = path.rpartition('/')
    return filename

assert basename('hello.py') == 'hello.py'
assert basename('./hello.py') == 'hello.py'
assert basename('../lesson3/hello.py') == 'hello.py'
assert basename('/hello.py') == 'hello.py'
assert basename('cat.jpg') == 'cat.jpg'
assert basename('hello/') == ''
assert basename('/home/taty/hello/') == ''
assert basename('/home/taty/hello') == 'hello'
assert basename('/home/taty/.gitignore') == '.gitignore'
assert basename('') == ''
