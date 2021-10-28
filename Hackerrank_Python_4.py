###Compare the Triplet###

def compareTriplets(a, b):
    # Write your code here
    Alice=0
    Bob=0
    for i in range(len(a)):
        if a[i] >b[i]:

            Alice +=1
        elif a[i] <b[i]: 
            Bob +=1    

    return Alice, Bob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
    
###Diagonal Difference ###


def diagonalDifference(arr):
    r=0
    l=0
    for i in range(n):
        r=r+arr[i][i]
        l=l+arr[i][n-1-i]
    return abs(r-l)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()   
    
### plus minus ###
def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0 
    zero=0
    for a in arr:
        if a>0: pos +=1
        elif a<0: neg +=1
        else: zero +=1
    print("{:.6f}". format(pos/n))
    print("{:.6f}". format(neg/n))
    print("{:.6f}". format(zero/n))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
### Mini-Max Sum ###
def miniMaxSum(arr):
    arr.sort()
    #return (sum(arr[1:]), sum(arr[:-1]))  returns tuple
    print (sum(arr[:-1]), sum(arr[1:]))
    

    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
### Birthday Cake Candles ###
def birthdayCakeCandles(candles):
    # Write your code here
    m=sorted(candles,  reverse=True)   #m=list.sort() --> m=None and m is already update but sorted returns the list
    count=0
    for a in m:
        if a ==m[0]:
            count+=1
        else:break
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

### Time Conversion ###
def timeConversion(s):
    # Write your code here
    if s[-2:]=='PM':
        if s[:2]!='12':
            s = str(int(s[:2]) + 12) + s[2:-2]
        else:
            s=s[:-2]
    else:
        if s[:2]=='12':
            s = '00' + s[2:-2]
        else:
            s=s[:-2]
    return (s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()    
    
###  Grading Students ###
 def gradingStudents(grades):
    new_grade=[]
    for a in grades:
        if a < 38:
            new_grade.append(a)
        elif a%5 <3:
            new_grade.append(a)
        else:
            new_grade.append(5*int(1+a/5)) 
    return (new_grade)        
      


    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close() 
    
### Apple and Orange ###
import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
     

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app_cnt=0
    org_cnt=0
    for i in apples:
        if i+a >=s and i+a <=t: app_cnt +=1
    for j in oranges:
        if j+b >=s and j+b <=t: org_cnt +=1
    print(app_cnt)
    print(org_cnt)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)   
    
###   Number Line Jumps ###
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 <= v2 and (v1+x1)<(v2+x2):
        return ('NO')     
    else:
        k1=v1+x1
        k2=v2+x2
        while (k1)<(k2):
            k1=k1+v1
            k2=k2+v2
        if k1==k2:    
            return ('YES')
        else:
            return ('NO')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
 
################
#find lcm, least common multiple, for multiple numbers#
arr=[24,18,6,9]
arr=sorted(arr)
lcm=set()
n=4

for i in range(n - 1):
    lcm.add(compute_gcd(arr[i], arr[i+1]))
m=list(lcm)
for i in sorted(m):
    for j in arr:
        if j%i !=0:
            lcm.remove(i)
            break
print(min(lcm))    
### Between Two Sets###    
def getTotalX(a, b):
    count = 0
    flag = True
    for i in range(a[len(a)-1], b[0]+1):
        for j in a:
            if i%j != 0:
                flag = False
                break
        if flag:
            for j in b:
                if j%i != 0:
                    flag = False
                    break 
        if flag:
            count += 1
        flag = True    
    return count       
    
### Breaking the records ###

def breakingRecords(scores):
    # Write your code here
    Max_s=scores[0]
    Min_s=scores[0]
    cnt_min=0
    cnt_max=0
    for a in scores:
        if a < Min_s:
            cnt_min +=1
            Min_s=a
        if a > Max_s:
            cnt_max +=1
            Max_s =a
    return cnt_max, cnt_min
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

###Sales by Match###

def sockMerchant(n, ar):
    # Write your code here
    pair=0
    sett=list(set(ar))
    for i in range(len(sett)):
        count=ar.count(sett[i])
        pair=count//2+pair
    return pair   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

####Counting Valleys ###
def countingValleys(steps, path):
    # Write your code here
    level=0
    valleys=0
    for direction in path:
        if direction=="U":
            level+=1
            if level==0:
                valleys +=1
        else:
            level -=1  
    return valleys   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

###Electronics Shop###
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    price = -1
    k = sorted(keyboards, reverse=True)
    d = sorted(drives, reverse=True)
    for i in range(len(k)):
        for j in range(len(d)):
            if k[i] + d[j] <= b:
                if k[i] + d[j] > price:
                    price = k[i] + d[j]
                break
    return price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
### Cats and a Mouse ###
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x-z) < abs (y-z):
        return 'Cat A'
    elif abs(x-z) > abs (y-z):
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
###  Forming a Magic Square ###

a1= [[8,1,6],[3,5,7],[4,9,2]]
a2=[[0,0,0],[0,0,0],[0,0,0]]
a3=[[0,0,0],[0,0,0],[0,0,0]]    
a4=[[0,0,0],[0,0,0],[0,0,0]]
a5=[[0,0,0],[0,0,0],[0,0,0]]
a6=[[0,0,0],[0,0,0],[0,0,0]]
a7=[[0,0,0],[0,0,0],[0,0,0]]
a8=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        a2[i][j]=a1[i][2-j]
        a3[i][j]=a1[2-i][j]
        a4[i][2-j]=a3[i][j]
        a5[i][j]=a1[j][2-i]
        a6[i][2-j]=a5[i][j]
        a7[2-i][j]=a5[i][j]
        a8[2-i][2-j]=a7[2-i][j]

def formingMagicSquare(s):
    # Write your code here  
    Fcost=100
    for j in (a1,a2,a3,a4,a5,a6,a7,a8):
         cost=0  
         for i in range(3):
             cost+=(sum(abs(a - b) for a,b in zip(s[i], j[i])))
         if Fcost >=cost:
             Fcost=cost
    return Fcost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
        print(s)

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

#### generate magic square n(n2+1)/2###
M = n(n2+1)/2


def generateSquare(n):
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]

    # initialize position of 1
    i = n / 2
    j = n - 1

    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0

            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1  # 1st condition

    # Printing magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) / 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                  end='')

            # To display output
            # in matrix form
            if j == n - 1:
                print()


# Driver Code


# Works only when n is odd
n = 7
generateSquare(n)

# This code is contributed
# by Harshit Agrawal 
 ---------------------------------------------------
###Climbing the Leaderboard###
#This solution failed the time limit
def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked=set(ranked)
    lst=[]
    for a in player:
        ranked.add(a)
        r_list=(sorted(list(ranked),reverse=True))
        for i in range(len(r_list)):
            if r_list[i] == a:
                lst.append(i+1)
    return lst
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
### This solution use bisect
from bisect import bisect_right

def climbingLeaderboard(ranked, player):
    lst=[]
    # Write your code here
    scores=sorted(set(ranked))
    for i in player:
        lst.append(len(scores)-bisect_right(scores,i)+1)
    return lst   
    
### The Hurdle Race ###
def hurdleRace(k, height):
    if max(height)-k <=0:
     return 0
    else:
     return   max(height)-k
        
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])
    
    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
 ###  Designer PDF Viewer ###
 
 alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def designerPdfViewer(h, word):
    # Write your code here
    di=dict(zip(alp, h))
    hh=0
    for i in word:
        if di[i] > hh:
            hh = di[i]
    return hh*len(word)        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
 
 ### Utopian Tree###
 
 def utopianTree(n):
    # Write your code here
    
    if n ==0:
        return 1
    else:
        h=1
        for i in range(1,n+1):
            if i%2!=0:
                h = 2*h
            else:
                h +=1
    return h             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
    
### Angry Professor ###

#in one line
#return('YES' if len([i for i in a if i<=0])<k else 'NO')

def angryProfessor(k, a):
    # Write your code here
    cnt=0
    for i in a:
        if i<=0:
            cnt+=1
    if cnt >=k:
        return 'NO'
    else:
        return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
### Beautiful days at the movies ###
def beautifulDays(i, j, k):
    # Write your code here
    cnt=0
    for d in range(i,j+1):
        if abs(d-int(str(d)[::-1]))%k==0:
            cnt +=1
    return cnt        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
    
###Viral Advertising ###
def viralAdvertising(n):
    # Write your code here
    total = 2;
    liked = 2;
    for _ in range(n-1):
        liked = liked * 3//2
        total += liked
    return total

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

###Repeated String###
def repeatedString(s, n):
    # Write your code here
    #s=((n//len(s))+1)*s
    #return s[0:n].count('a')  doesnt work for large n
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
###jumpingOnClouds###
def jumpingOnClouds(c):               
    # Write your code here
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()   

###Divisible sum pair ###

def divisibleSumPairs(n, k, ar):
    # Write your code here
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                cnt +=1
    return cnt    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

### Subarray Division ###  

def birthday(s, d, m):
    # Write your code here
    cnt=0
    for i in range(len(s)-m+1):
        if (sum(s[i:i+m]))%d==0:
            cnt +=1
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
    
### Migratory Birds ###   
-----
#solution too slow
import collections
def migratoryBirds(arr):
    # Write your code here
    my_dict=collections.Counter(arr)
    for key, value in my_dict.items():
        if value == max(my_dict.values()):
            return key
-----    
def migratoryBirds(arr):
    # Write your code here
    cnt=[]
    x = list(set(arr))
    for i in x:
        cnt.append(arr.count(i))
    return(x[cnt.index(max(cnt))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

### Non-Divisible Subset ###   

from collections import Counter
def nonDivisibleSubset(k, s):
    # Write your code here
    if k == 1 or len(s) == 1:
        return 1
    S = [item % k for item in s]
    d = Counter(S)
    ans1, ans2 = 0, 0
    if 0 in d or k in d:
        ans1 += 1
    if 0 in d:
        del d[0]
    if k in d:
        del d[k]
    if k % 2 == 0 and k // 2 in d:
        ans1 += 1
        del d[k // 2]
    for num in d:
        if k - num not in d:
            ans1 += d[num]
        else:
            ans2 += max(d[num], d[k - num])

    return ans1 + ans2 // 2


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

### Day of the Programmer ###

def dayOfProgrammer(year):
    # Write your code here
    if year > 1918:
        if year%4==0 and year%100!=0:
            return '12.09.'+str(year)
        elif year%4==0 and year%400==0:
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
    elif year==1918:
        return "26.09.1918"
    else:
        if year%4==0:
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
                
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

### Bill Division ###

def bonAppetit(bill, k, b):
    # Write your code here
    bill.remove(bill[k])
    m = abs(b-sum(bill)/2)
    if m==0:
        print ("Bon Appetit")
    else:
        
        print (int(m))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

### Leap year ###
def is_leap(year):
    leap = False
    if year % 4 == 0 and year %400 ==0:
        leap = True
    elif year %4 == 0 and year %100 !=0:
        leap = True
    else:
        leap = False

        # Write your logic here

    return leap
###    

    