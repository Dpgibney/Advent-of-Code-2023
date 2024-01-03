import copy

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')

Lines = file1.read().splitlines()
split = Lines.index('')
funcs_in = Lines[:split]
parts_in = Lines[split+1:]
key_map = {'x':0,'m':1,'a':2,'s':3}

def calc_pos(arrays):
    tmp = 1
    for i in range(len(arrays)):
        tmp *= len(arrays[i]) 
        print(len(arrays[i]))
    print("A: ",tmp)
    return tmp

funcs = {}
def make_fun(elif_,else_):

    def f(part):
        tmp_val = 0
        for path in elif_:
            tmp_part = copy.deepcopy(part)
            key = path[0]
            sym = path[1]
            path = path[2:]
            path, new_workflow = path.split(':')
            val = int(path)
            print(key,sym,val,new_workflow,len(part[0]),len(part[1]),len(part[2]),len(part[3]))
            if sym == '>':
                #print('greater')
                for pos_val in range(1,val+1):
                    try:
                        tmp_part[key_map[key]].remove(pos_val)
                    except:
                        pass
                if new_workflow == 'A':
                    tmp_val += calc_pos(tmp_part)
                elif new_workflow == 'R':
                    pass
                else:
                    tmp_val += funcs[new_workflow](copy.deepcopy(tmp_part))

                for pos_val in range(val+1,4001):
                    try:
                        part[key_map[key]].remove(pos_val)
                    except:
                        pass

            else:
                #print('lesser')
                for pos_val in range(val,4001):
                    try:
                        tmp_part[key_map[key]].remove(pos_val)
                    except:
                        pass
                if new_workflow == 'A':
                    tmp_val += calc_pos(tmp_part)
                elif new_workflow == 'R':
                    pass
                else:
                    tmp_val += funcs[new_workflow](copy.deepcopy(tmp_part))

                for pos_val in range(1,val):
                    try:
                        part[key_map[key]].remove(pos_val)
                    except:
                        pass

        #print("else: ",else_)
        if else_ == 'A':
            return tmp_val + calc_pos(part)
        elif else_ == 'R':
            return tmp_val
        else:
            return tmp_val + funcs[else_](copy.deepcopy(part))
    return f

for func in funcs_in:
    key, func = func.strip('}').split('{')
    func = func.split(',')
    #if_ = func.pop(0)
    else_ = func.pop(-1)
    elif_ = func

    f = make_fun(elif_.copy(),else_)
    funcs.update({key:f})

valid = [[i for i in range(1,4001)] for j in range(4)]
print(funcs['in'](valid))
    
