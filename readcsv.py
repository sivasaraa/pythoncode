import csv


with open('mpg.csv') as csvfile:
    mpgs = list(csv.DictReader(csvfile))


print("no of rows",len(mpgs))
print("list of column names",mpgs[0].keys())

print("avg city milege")
print(sum(float(d['mpg']) for d in mpgs)/len(mpgs))

print("milege calculatoion based on cylinders")
result = [];
cyl = set(d['cylinders'] for d in mpgs)
for c in cyl:
    totalmpg = 0
    count = 0
    for d in mpgs:
        if d['cylinders'] == c:
            totalmpg += float(d['mpg'])
            count+=1
    result.append((c,totalmpg/count))

result.sort(key=lambda s:s[0])
print(result)

print("milege based on vehicle")
veh = set(d['name'] for d in mpgs)
result = []
for v in veh:
    totalmpg = 0
    count = 0
    for d in mpgs:
        if d['name'] == v:
            totalmpg += float(d['mpg'])
            count += 1
    result.append((v,totalmpg/count))
result.sort()
print(result)