import csv

with open('mpg.csv') as csvfile:
    mpgfile = list(csv.DictReader(csvfile))

print(len(mpgfile))
print(mpgfile[0].keys())

avgmpg = sum(float(d['mpg']) for d in mpgfile)/len(mpgfile)
print("average milege",avgmpg)

unicyl = set(d['cylinders'] for d in mpgfile)
print("unique cylinders",unicyl )

print("finding the milege based on the cylinder")

result = []
for cyl in unicyl:
    totalmpg = 0
    count = 0
    for d in mpgfile:
        if d['cylinders'] == cyl:
            totalmpg += float(d['mpg'])
            count += 1
    result.append((cyl,totalmpg/count))
print("final result=",result)





