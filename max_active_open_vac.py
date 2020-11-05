from collections import defaultdict


ins_outs = defaultdict(str) #{}
count = int(input())

for i in range (count):
    start, end = input().split()
    start,end = int(start), int(end)
    ins_outs[start] += '(' 
    ins_outs[end] += ')'

ins_outs_sorted = {k: v for k, v in sorted(ins_outs.items(), key=lambda item: item[0])}
start = next(iter(ins_outs_sorted))
par_count = 0
open_par = 0
total = 0
max_par = 0
for i, time in enumerate(ins_outs_sorted):
    if ins_outs_sorted[time][0] == '(':
        open_par+=len(ins_outs_sorted[time])
        if open_par >= max_par:
            if open_par > max_par:
                total = 0
                par_count = 0
            max_par = open_par
            max_start = time
    else:
        if open_par == max_par:
            max_end = time
        open_par-=len(ins_outs_sorted[time])
        if open_par == 0:
            end = time
            par_count+=1
            duration = max_end-max_start+1
            total +=duration
            start = next(iter(ins_outs_sorted))
            
print (par_count, total)