L = []
for i in range(input()):
    line =input().split()
    if len(line) == 3:
        arg = 'L.' + line[0] + '(' + line[1] + ', ' + line[2] + ')'
    elif len(line) == 1:
        if line[0] == 'print':
            arg = 'print L'
        else:
            arg = 'L.' + line[0] + '()'
    elif len(line) == 2:
        arg = 'L.' + line[0] + '(' + line[1] + ')'

    exec(arg)