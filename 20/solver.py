import re

file1 = open('p1_input.txt','r')
#file1 = open('p1_input.example','r')
#file1 = open('p1_input.example2','r')

Lines = file1.read().splitlines()

'''I'm thinking I should store all modules in a dict and then call then with the singnal and the queue'''
'''module_format is [type,[outputs]]'''

class module:
    def __init__(self,module_format):
        print(module_format)
        self.memory = {}
        self.mod_type = module_format[0]
        self.outputs = module_format[1]
        self.sender = module_format[2]
        self.state = 'off'
        self.memory = {}

    def run(self,pulse,sender,queue):
        #print("pulse: ",pulse,"sender: ",sender,"quueue: ",queue)
        highs = 0
        lows = 0
        if   self.mod_type == 'broadcaster':
            for output in self.outputs:
                queue.append([output,pulse,self.sender])
                lows += 1
        elif self.mod_type == '%':
            if pulse == 1:
                pass
            else:
                if self.state == 'off':
                    for output in self.outputs:
                        queue.append([output,1,self.sender])
                        highs += 1
                    self.state = 'on'
                else:
                    for output in self.outputs:
                        queue.append([output,0,self.sender])
                        lows += 1
                        #print("awefasdf")
                    self.state = 'off'
        else:
            self.memory.update({sender:pulse})
            all_high = True
            for key in self.memory.keys():
                #print(sender)
                #print(self.memory)
                #print(self.memory[key])
                #print("key: ",key)
                if self.memory[key] == 0:
                    all_high = False
                    break
            if all_high:
                for output in self.outputs:
                    queue.append([output,0,self.sender])
                    lows += 1
            else:
                for output in self.outputs:
                    queue.append([output,1,self.sender])
                    highs += 1
        return lows,highs





key_pattern = re.compile('[a-z]*')

modules = {}
for line in Lines:
    strs = re.findall(key_pattern,line)

    to_del = []
    for sub_indx, substr in enumerate(strs):
        if substr == '':
            to_del.append(sub_indx)
    for i in to_del[::-1]:
        del strs[i]
    #print(strs)

    key = strs[0]
    if strs[0] == 'broadcaster':
        mod_type = 'broadcaster'
    else:
        mod_type = line[0]
    outputs = strs[1:]
    modules.update({key:module([mod_type,outputs,key])})

sig_que = [['broadcaster',0,None]]
tmp = 0
low,high = 0,0
for push in range(100000):
    if push % 1000 == 0:
        print(push//1000)
    low += 1
    sig_que = [['broadcaster',0,None]]
    tmp = 0
    while sig_que:
        #print("cur que: ",sig_que)
        tmp_low = 0
        tmp_high = 0
        if sig_que[0][0] in modules.keys():
            tmp_low, tmp_high = modules[sig_que[0][0]].run(sig_que[0][1],sig_que[0][2],sig_que)
        #print(tmp_low,tmp_high)
        low += tmp_low
        high += tmp_high
        del sig_que[0]
        tmp += 1
#print(low,high)

for key in modules:
    modules[key].state = 'off'
    for i in modules[key].memory:
        modules[key].memory[i] = 0

print("second run")
low,high = 0,0
for push in range(1,1000000000):
    low += 1
    sig_que = [['broadcaster',0,None]]
    tmp = 0
    while sig_que:
        #print("cur que: ",sig_que)
        tmp_low = 0
        tmp_high = 0
        if sig_que[0][0] in modules.keys():
            tmp_low, tmp_high = modules[sig_que[0][0]].run(sig_que[0][1],sig_que[0][2],sig_que)
        #print(tmp_low,tmp_high)
        low += tmp_low
        high += tmp_high
        del sig_que[0]
        tmp += 1
        for item in sig_que:
            if item[0] == 'rx':
                if item[1] == 0:
                    print(push)
                    input()
                    exit()
    #print(push,modules['ql'].memory)
    #print(modules['vm'].memory)
    #if modules['ql'].memory['rl'] == 1:
    #    print(push,modules['ql'].memory['rl'])
    #    exit()

    for key in modules['zg'].memory.keys():
        if modules['zg'].memory[key] == 1:
            print(push,modules['zg'].memory())
            exit()

    #print(modules['zg'].memory)
    #if push == 4096:
    #    exit()
    
print(low,high)
