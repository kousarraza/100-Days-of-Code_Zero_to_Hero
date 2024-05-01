# 94.Write a python to print the first ten numbers square,cube and their sum.

snum=ssquare=scube=0
print("Number\t","Square\t","Cube")
print("----------------------------------------")
for i in range(1, 11):
    print(i, "\t", i*i, "\t", i*i*i)
    snum+=i
    ssquare+=i*i
    scube+=i*i*i
print("----------------------------------------")
print(snum,"\t",ssquare,"\t",scube)