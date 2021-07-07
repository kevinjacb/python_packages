from rich import print 
import sys
import os
import tabulate

# files = []
corr_path = []
parts = []

for path in sys.path:
    try:
        for file in os.listdir(path):
            if '-info' in file: 
                # files.append(file.replace('dist',''))
                corr_path.append(str(path))
                parts.append(file.replace('.dist','').split('-'))    
    except:
        continue

maxes = [0,0]

for component in parts:
    if maxes[0] < len(component[0]):
        maxes[0] = len(component[0])
    if maxes[1] < len(component[1]):
        maxes[1] = len(component[1])
    
maxes.append(len(max(corr_path,key=len)))

raw_data = []
data = []

for i,component in enumerate(parts):
    t_data = []
    t_data.append('[bold yellow]'+component[0]+'[/bold yellow]')
    t_data.append('[bold cyan]'+component[1]+'[/bold cyan]')
    t_data.append('[bold blue]'+corr_path[i]+'[/bold blue]')
    data.append(t_data)
    t_data = []
    t_data.append(component[0])
    t_data.append(component[1])
    t_data.append(corr_path[i])
    raw_data.append(t_data)
    

# print(data)
table = tabulate.make_table(raw_data= raw_data,rows=data, labels=['Package','Version','Path'],centered=True)
print(table)
