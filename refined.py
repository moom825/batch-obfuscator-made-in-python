from os import getcwd
from random import randrange
from re import finditer
from subprocess import run


temp = input("Path of the Batch File >\t").strip()  # "sample.bat"
with open(temp) as temp:
    data = temp.read()
temp = "would you like to add random '^' to the obfuscation (may break script. not recommended) y or n (default n):\t"

if input(temp).strip().lower().startswith("y"):
    n = len(data)
    temp = list(data)
    for i in range(randrange(n)):
        temp.insert(i + randrange(n), "^")
    data = "".join(temp)

data += '\nset a = %%~i\nset a = % + %~i"%\nset a = %a%\n:aaaaaaaaaaaaaaaaaaaaaaaaaaaaab\n'
data = data.replace("%%~", "ckoco").replace("%~", "croco")

data = list(data)
temp = True
for index, item in enumerate(data):
    if item == "%":
        temp = not temp
        if temp:
            data[index] = "replaced"
del index, item
data = "".join(data)

res = [i.start() for i in finditer("%", data)]
temp = [i.start() for i in finditer("replaced", data)]
result = [(res[i], temp[i] + 8) for i in range(len(temp))]
del res
temp = [i.start() for i in finditer("croco", data)]
result += [(i, i + 7) for i in temp]
temp = [i.start() for i in finditer("ckoco", data)]
result += [(i, i + 7) for i in temp]
temp = ""
for i in data.splitlines():
    if i.startswith(":"):
        i += "\u044f"
    temp += i + "\n"
res = [i for i, j in enumerate(temp) if j.endswith("\u044f")]

j = -1
res1 = []
for i in temp.splitlines():
    if not i.startswith(":"):
        continue
    j += 1
    res1.append(res[j] - len(i) + 1)
del j, temp

for r in (res, res1):
    for index, item in enumerate(r[1:], start=1):
        r[index] = item - index
result += [(res1[i], res[i]) for i in range(len(res))]
del r, res, res1
result.sort()
result.insert(0, (0, 0))
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
offset = 0
n = len(result) - 1
for i in range(n + 1):
    start = result[i][1] + offset
    end = (result[i + 1][0] + offset) if i < n else len(data)
    tmp = data[start:end]
    tmp2 = len(tmp)
    for j, k in temp:
        tmp = tmp.replace(j, f"%r:~{k},1%")
    data = data[:start] + tmp + data[end:]
    offset += len(tmp) - tmp2
del end, n, offset, result, start, tmp2, tmp
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
    data[:-123],
)
del data
temp = "\n".join(temp)
name = input("enter output file name (do not include extention): ")  # "o"
with open(name + ".bat", "w") as f:
    f.write(temp)
temp = (
    rf'>"temp.~b64" echo(//4mY2xzDQo= && certutil.exe -f -decode "temp.~b64" "{name}tmp.bat" && del "temp.~b64" && copy "{name}tmp.bat" /b + "{getcwd()}\{name}.bat" /b',
    f"del {name}.bat /f && rename {name}tmp.bat {name}.bat",
)
for i in temp:
    run(i, shell=True, capture_output=True, stdin=-1)
print(f'saved to "{name}.bat"')
