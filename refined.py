from os import getcwd
from random import randrange
from re import finditer, sub
from subprocess import PIPE, run


class RepObj:
    def __init__(self, replace_by, every):
        self.__counter = 1
        self.__every = every
        self.__replace_by = replace_by

    def doit(self, m):
        rval = m.group(1) if self.__counter % self.__every else self.__replace_by
        self.__counter += 1
        return rval


def func():
    n = len(data)
    result = list(data)
    for i in range(randrange(n)):
        result.insert(i + randrange(n), "^")
    return "".join(result)


temp = "sample.bat"  # input("Path of the Batch File >\t").strip()
with open(temp) as temp:
    data = temp.read()
# temp = "would you like to add random '^' to the obfuscation (may break script. not recommended) y or n (default n):\t"
# data = func() if input(temp).strip().lower().startswith("y") else data
del temp

data += '\nset a = %%~i\nset a = % + %~i"%\nset a = %a%\n:aaaaaaaaaaaaaaaaaaaaaaaaaaaaab\n'
data = data.replace("%%~", "ckoco").replace("%~", "croco")
data = sub("(%)", RepObj("replaced", 2).doit, data)
res = [i.start() for i in finditer("%", data)]
temp = [i.start() for i in finditer("replaced", data)]
result = [(res[i], temp[i] + 8) for i in range(len(temp))]
del res
temp = [i.start() for i in finditer("croco", data)]
result += [(i, i+7) for i in temp]
temp = [i.start() for i in finditer("ckoco", data)]
result += [(i, i+7) for i in temp]
temp = ""
for i in data.splitlines():
    if i.startswith(":"): i += "\u044f"
    temp += i + "\n"
res = [i for i, j in enumerate(temp) if j.endswith("\u044f")]

j = -1
res1 = []
for i in temp.splitlines():
    if not i.startswith(":"): continue
    j += 1
    res1.append(res[j] - len(i) + 1)
del j, temp

for r in (res, res1):
    for index, item in enumerate(r[1:], start=1):
        r[index] = item - index
result += [(res1[i], res[i]) for i in range(len(res))]
del res, res1
result.sort()
result.insert(0, (0, 0))
result2 = [(result[i][1], result[i+1][0]) for i in range(len(result)-1)]
result2.append((result[-1][1], int("9"*20)))
temp = (
    ("J", 0),
    ("g", 1),
    ("i", 2),
    ("t", 4),
    ("G", 5),
    ("X", 6),
    ("z", 7),
    ("s", 8),
    ("w", 9),
    ("b", 10),
    ("h", 11),
    ("m", 12),
    ("u", 13),
    ("S", 14),
    ("H", 15),
    ("I", 16),
    ("O", 17),
    ("A", 18),
)
staticnum = 0
for i in range(len(result2)):
    start = int(result2[i][0]) + staticnum
    end = int(result2[i][1]) + staticnum
    tmp = data[start:end]
    test2tmp = len(tmp)
    for j, k in temp:
        tmp = tmp.replace(j, f"%r:~{k},1%")
    data = data[:start] + tmp + data[end:]
    staticnum += len(tmp) - test2tmp
del result2, staticnum, start, end, test2tmp, tmp
temp = (("ckoco", "%%~"), ("croco", "%~"), ("replaced", "%"))
for i, j in temp:
    data = data.replace(i, j)
temp = (
    "@%pUBlIc:~89,83%%PUBLic:~5,1%CHo^ of^%PuBlIC:~46,16%f",
    # "@%pUBlIc:~89,83%%PUBLic:~5,1%CHo of%PuBlIC:~46,16%f"
    # "@%public:~89,83%%public:~5,1%cho of%public:~46,16%f"
    # %public% = C:\Users\Public  # default in Windows
    # %str_var:~a,b% = '' if a > len(str_var) else str_var[a:a+b]
    # "@%public:~5,1%cho off" # "@eCHo off" # "@echo off"
    "SEt R^=Jg^%pUBLIc:~13,1%^gtGXz%pUBLIc:~4,1%w%pUBLIc:~11,1%^hm%pUBLIc:~10,1%^S^HI^O^A",
    # "SEt R=Jg%pUBLIc:~13,1%gtGXz%pUBLIc:~4,1%w%pUBLIc:~11,1%hm%pUBLIc:~10,1%SHIOA"
    # "set r=jg%public:~13,1%gtgxz%public:~4,1%w%public:~11,1%hm%public:~10,1%shioa"
    # "set r=jg^%public:~13,1%^gtgxz^%public:~4,1%^w^%public:~11,1%^hm^%public:~10,1%^shioa"
    # "SEt R=JgigtGXzswbhmuSHIOA" # "set r=jgigtgxzswbhmushioa"
    "^%pUBlIC:~14,1%^L%pUBliC:~55,17%^%publIc:~4,1%",
    # "%pUBlIC:~14,1%L%pUBliC:~55,17%%publIc:~4,1%"
    # "%public:~14,1%l%public:~55,17%%public:~4,1%"
    # "%public:~14,1%l%public:~4,1%" # "cLs" # "cls"
    "@^e^c%r:~15,1%^%r:~17,1% ^%r:~17,1%n",
    # "@ec%r:~15,1%%r:~17,1% %r:~17,1%n" # "@ecHO On" # "@echo on"
    data,
)
temp = "\n".join(temp)
name = "o"  # input("enter output file name (do not include extention): ")
with open(name + ".bat", "w") as f:
    f.write(temp)
temp = (
    rf'>"temp.~b64" echo(//4mY2xzDQo= && certutil.exe -f -decode "temp.~b64" "{name}tmp.bat" && del "temp.~b64" && copy "{name}tmp.bat" /b + "{getcwd()}\{name}.bat" /b',
    f"del {name}.bat /f && rename {name}tmp.bat {name}.bat",
)
# for i in temp:
#     run(i, shell=True, capture_output=True, stdin=PIPE)
print(f'saved to "{name}.bat"')
