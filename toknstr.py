import shlex
s = 'xyz abc mnp "asdf dfaa asdf" asd "fdasasdsdaff"'
for i in shlex.split(s,posix=False):
    print i
