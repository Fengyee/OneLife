import sys, os
import re

def func(id):
  if id < 26:
    return str(chr(id+65))
  else:
    return func(id//26) + func(id - (id//26)*26)

dir = "D:\SteamLibrary\steamapps\common\One Hour One Life\objects"
files = [file for file in os.listdir(dir) if re.match('[0-9].*', file)]

result = []
for file in files:
  with open(dir+'\\'+file) as f:
    id = f.readline().rstrip()[3:]
    name = f.readline().rstrip()
    new_id = func(int(id))[::-1]
  result.append([id, name, new_id])


with open(".\\table.csv", 'w+') as f:
  f.write("Id,Description,Code\n")
  for record in result:
    f.write(record[0]+','+record[1]+','+record[2]+'\n')



