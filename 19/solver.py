file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()
split = Lines.index('')
funcs_in = Lines[:split]
parts_in = Lines[split+1:]

print(funcs_in)
print(parts_in)

class Parts:
    def __init__(self,xmas):
        self.xmas = xmas

funcs = {}
def make_fun(elif_,else_):

    def f(part):
        for i in elif_:
            key = i[0]
            sym = i[1]
            i = i[2:]
            i, new_workflow = i.split(':')
            val = int(i)
            #print(key,sym,val,new_workflow)
            if sym == '>':
                #print('greater')
                if part.xmas[key] > val:
                    if new_workflow == 'A' or new_workflow == 'R':
                        return new_workflow
                    return funcs[new_workflow](part)
            else:
                #print('lesser')
                if part.xmas[key] < val:
                    if new_workflow == 'A' or new_workflow == 'R':
                        return new_workflow
                    return funcs[new_workflow](part)
        #print("else: ",else_)
        if else_ == 'A' or else_ == 'R':
            return else_
        else:
            return funcs[else_](part)
    return f

for func in funcs_in:
    key, func = func.strip('}').split('{')
    func = func.split(',')
    #if_ = func.pop(0)
    else_ = func.pop(-1)
    elif_ = func

    f = make_fun(elif_.copy(),else_)
    funcs.update({key:f})

parts = []
for part in parts_in:
    attr = part.strip('{}').split(',')
    x = 0
    m = 0
    a = 0
    s = 0
    xmas = {}
    for i in attr:
        i = i.split('=')
        xmas.update({i[0]:int(i[1])})
    part = Parts(xmas)
    parts.append(part)

count = 0
for part in parts:
    tmp = 0
    if funcs['in'](part) == 'A':
        tmp += part.xmas['x']
        tmp += part.xmas['m']
        tmp += part.xmas['a']
        tmp += part.xmas['s']
        print(tmp)
        count += tmp
print(count)

    
    
