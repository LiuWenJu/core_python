#coding=utf-8

import random
import time

n = int(raw_input("你需要多少次的车速："))
List = []
s = 0
i = 0
#for i in range(5):
while i < n:
    r = random.randint(1,300)
    #s = r
    if 0<= r <=200:
        
        print "你的车在正常行驶"
    else:
        print "Dangoures!"
    
    List.append(r)
    time.sleep(1)
    print "你的车速是:",r
    time.sleep(3)
    #s += s
    s = r + s
    i += 1
print List
#print List.sort()

print "你的平均车速是",float(s/n)
