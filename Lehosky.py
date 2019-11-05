from math import floor,ceil

print("\n***************************Lehosky Test***************************\n")

t1 = (40,100,100)   #execution time,time period,deadline
t2 = (40,150,150)
t3 = (100,350,350)

no_task = 3
#PRIORITY T1 > T2 > T3
period = [ t1[1],t2[1],t3[1] ]          #values entered in priority order
execution = [ t1[0],t2[0],t3[0] ]       #values entered in priority order
deadline = [ t1[2],t2[2],t3[2] ]

for t in range(no_task):
    print("task "+ str(t) +" -> exe time: "+ str(execution[t]) +" period: "+ str(period[t]) + " deadline: "+ str(deadline[t]))
print("\n")

#data structure to hold all s values for each task
s = []
for a in range(no_task):
    s.append([])

#main algorithm to compute s
for i in range(no_task):
    for j in range(i+1):
        for k in range(1,floor(period[i]/period[j])+1):
            s[i].append( (k)*period[j] )
            
print("value of time period (s) calculated as follows: ")
for i,temp in enumerate(s):
    print("Task "+ str(i) +" : ",temp)

def w(t,n):
    ans = 0
    for i in range(n):
        ans += execution[i]*ceil(t/period[i])
    return ans

print("\n")
for i,task in enumerate(s):
    flag = 0
    for t in task:
        if w(t,i+1) <= t:
            flag = 1
            print("Task "+str(i+1)+" is schedulable: w = "+str( w(t,i+1) )+" <= "+str(t))
            break
    if flag == 0:       
        print("Task "+str(i+1)+" is not schedulable")   
            