import time
import pyfiglet
import subprocess
import os
import easygui
from tqdm import tqdm
print(pyfiglet.figlet_format("batch obuscator by moom825"))
print("please pick a batch file")
time.sleep(2)
file = easygui.fileopenbox()
file = open(file,mode='r')
DNA = file.read()
file.close()
yorn = input("would you like to add random ^ to the obfuscation(may break script. not recommended) y or n: ")
if yorn == "n":
    isittrueorfalse = False
    number = 2
elif yorn == "y":
    isittrueorfalse = True
    number = input("please enter the number of ^ you want(you can not have more than the length of your text): ")
    number = int(number)
else:
    print("that is not a correct option. now exiting...")
    exit()
letters = """SEt R^=Jg^%pUBLIc:~13,1%^gtGXz%pUBLIc:~4,1%w%pUBLIc:~11,1%^hm%pUBLIc:~10,1%^S^HI^O^A"""
echooff = """@%pUBlIc:~89,83%%PUBLic:~5,1%CHo^ of^%PuBlIC:~46,16%f"""
clss = """^%pUBlIC:~14,1%^L%pUBliC:~55,17%^%publIc:~4,1%"""
echoon = """@^e^c%r:~15,1%^%r:~17,1% ^%r:~17,1%n"""
def carrot():
    import random
    num_spaces = number
    assert(num_spaces <= len(DNA) - 1)
    space_idx = []
    space_idx.append(random.randint(0, len(DNA) - 2))
    num_spaces -= 1
    while (num_spaces > 0):
        idx = random.randint(0, len(DNA) - 2)
        if (not idx in space_idx):
            space_idx.append(idx)
            num_spaces -= 1
    result_with_spaces = ''
    for i in range(len(DNA)):
        result_with_spaces += DNA[i]
        if i in space_idx:
            result_with_spaces += '^'
    return result_with_spaces
result1 = []
import re
if isittrueorfalse == True:
    result_with_spaces = carrot()
    s = result_with_spaces
elif isittrueorfalse == False:
    result_with_spaces = DNA
    s = result_with_spaces
class RepObj:
    def __init__(self,replace_by,every):
        self.__counter = 1
        self.__every = every
        self.__replace_by = replace_by

    def doit(self,m):
        rval = m.group(1) if self.__counter % self.__every else self.__replace_by
        self.__counter += 1
        return rval
s = s + """\nset a = %%~i\nset a = % + %~i"%\nset a = %a%\n:aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"""
s = s.replace('%%~', 'ckoco')        
s = s.replace('%~', 'croco')
r = RepObj("replaced",2)
result = re.sub("(%)",r.doit,s)
new_str = result
#print(new_str)
example = result
searching_for = "%"
searching_for1 = "replaced"
res = [i.start() for i in re.finditer(searching_for, example)]
res2 = [i.start() for i in re.finditer(searching_for1, example)]
itorator = -1
while True:
    itorator = itorator + 1
    result1.append(str(res[itorator]) + ":" + str(res2[itorator] + 8))
    if itorator == len(res2) - 1:
        break
result82 = new_str
new_str2 = result82
example82 = result82
searching_for1 = "croco"
res1 = [i.start() for i in re.finditer(searching_for1, example82)]
itorator = -1
while True:
    itorator = itorator + 1
    result1.append(str(res1[itorator]) + ":" + str(res1[itorator] + 7))
    if itorator == len(res1) - 1:
        break
searching_for12 = "ckoco"
res12 = [i.start() for i in re.finditer(searching_for12, example82)]
itorator = -1
while True:
    itorator = itorator + 1
    result1.append(str(res12[itorator]) + ":" + str(res12[itorator] + 7))
    if itorator == len(res12) - 1:
        break
newerman = ""
for i in example82.splitlines():
    if i[0:1] == ":":
        i = i + "\u044f" + "\n"
        newerman = newerman + i
    else:
        i = i + "\n"
        newerman = newerman + i
#print(newerman)
#searching_for = ":"
#searching_for1 = "\u044f"
charcount = 0
#res777 = [i for i in range(len(newerman)) if newerman[i].startswith('\n:')]
#print(res777)
res777 = []
res432 = [i for i in range(len(newerman)) if newerman[i].endswith('\u044f')]
#print(res432)
indi = -1
for i in newerman.splitlines():
    if i[0:1] == ":":
        indi = indi + 1
        e = res432[indi]
        ok = ((len(i) - 1) - 1)
        almoast = ((e - ok) - 1)
        res777.append(almoast)
#print(res777)
res324 = []
into = 0
into2 = 0
for i in res432:
    into2 = into2 + 1
    if into2 >= 2:
        into = into + 1    
        res324.append(i - into)
    else:
        res324.append(i)
res432 = res324
res3242 = []
into2 = 0
into22 = 0
for i in res777:
    into22 = into22 + 1
    if into22 >= 2:
        into2 = into2 + 1    
        res3242.append(i - into2)
    else:
        res3242.append(i)
res777 = res3242
#print(res777)
#print(res432)
#print(res432)
#print(res777)
itorator = -1
while True:
    itorator = itorator + 1
    result1.append(str(res777[itorator]) + ":" + str(res432[itorator]))
    if itorator == len(res432) - 1:
        break      
#print(result1)
#print(result82)
result23 = []
result1.append("0:0")
for i in result1:
    result23.append(i.replace(":","1479127489164718487184127487168721401"))
tmp = []
for i in result23:
    i = int(i)
    tmp.append(i)
result1 = sorted(tmp)
result23 = []
for i in result1:
    i = str(i)
    result23.append(i.replace("1479127489164718487184127487168721401",":"))
result1 = result23
#print(result1)
intorator = -1
result2 = []
try:
    while True:
        intorator = intorator + 1
        i1 = (result1[intorator].split(":"))[1]
        i2 = (result1[intorator+1].split(":"))[0]
        result2.append(i1+":"+i2)
        if intorator == len(result1) - 1:
            break
except:
    a = 1
result2.append((result1[intorator].split(":"))[1]+":"+"99999999999999999999")
DNA = new_str
intorator2 = -1
intorator22 = 0
num = 0
staticnum = 0
#print(result2)
#print(DNA)
test3 = 0
while True:
    intorator22 = intorator22 + 1
    intorator2 = intorator2 + 1
    #print("loop:" + str(intorator22))
    if intorator2 == len(result2) -1:
        break
    #print(intorator2)
    #print(intorator22)
    test1 = int(result2[intorator2].split(":")[0])
    test1 = test1 + staticnum
    test2 = int(result2[intorator2].split(":")[1])
    test2 = test2 + staticnum
    test3 = test1
    test4 = test2
    #print(DNA)
    #print(str(test3) + ":" + str(test4))
    tmp = DNA[test3:test4].replace("J","""%r:~0,1%""")
    test2tmp = len(tmp)
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    ##DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("G","""%r:~5,1%""")
    ##subandadd = len(tmp) - len(tmp)
    ##test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("g","""%r:~1,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("i","""%r:~2,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("I","""%r:~16,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("t","""%r:~4,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("X","""%r:~6,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("z","""%r:~7,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("S","""%r:~14,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("s","""%r:~8,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("w","""%r:~9,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("b","""%r:~10,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("h","""%r:~11,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("H","""%r:~15,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("m","""%r:~12,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("u","""%r:~13,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("O","""%r:~17,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    #DNA = DNA[:test1] + tmp + DNA[test2:]
    tmp = tmp.replace("A","""%r:~18,1%""")
    #subandadd = len(tmp) - len(tmp)
    #test4 = test4 + subandadd
    DNA = DNA[:test1] + tmp + DNA[test2:]
    #print(test2)
    #print(test3)
    #print(str(test1) + ":" + str(test2))
    staticnum = ((len(tmp) - test2tmp) + staticnum)
    num = len(tmp) - test2tmp
    #print(num)
    #print(tmp)
DNA = DNA.replace("ckoco", "%%~")
DNA = DNA.replace("croco", "%~")
DNA = DNA.replace("replaced", "%")
name = input("enter output file name(do not include extention): ")
for i in tqdm(range(10)):
    time.sleep(2)
f = open(name+".bat", "w")
poggers = echooff + "\n" + letters + "\n" + clss + "\n" + echoon + "\n" + DNA + "\n"
f.write(poggers)
f.close()
ok = os.getcwd()
bruh1 = r'>"temp.~b64" echo(//4mY2xzDQo= && certutil.exe -f -decode "temp.~b64" "{namee}tmp.bat" && del "temp.~b64" && copy "{namee}tmp.bat" /b + "{okk}\{namee}.bat" /b'.format(namee = name, okk = ok)
bruh2 = "del {namee}.bat /f && rename {namee}tmp.bat {namee}.bat".format(namee = name)
outputthatgoesnkowshere = subprocess.run(bruh1, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
outputthatgoesnkowshere = subprocess.run(bruh2, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
time.sleep(2)
print("saved to the file name " + '"' + name + ".bat" + '"')
#output = subprocess.run("chcp 936>nul && type "+name+".bat", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#output2 = subprocess.run("chcp 936>nul && type "+name+".bat", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#print(str(output2.stdout.decode('CP936')))
print("The operation is complete")
print("thank you for using, now exiting...")
exit()

