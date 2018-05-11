#considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms
import time


def Fibonacci():
    
    num = 1    
    prevNum = 1
    curr = 0
    arrayOfNum = []
    sum = 0
    arrayOfNum.append(num)
    while num < 4000000:   
        curr = num        
        num = num + prevNum
        prevNum = curr
        if num %2 ==0:
            sum += num
            arrayOfNum.append(num)    
    return 'Sum:',sum,'Fibonacci Numbers:',arrayOfNum

if __name__ == "__main__" :
    t = time.time()
    print Fibonacci()
    t1 = time.time()
    print 'diff in ms:', (t1 - t)