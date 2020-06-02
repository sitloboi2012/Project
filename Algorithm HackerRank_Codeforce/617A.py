#problem 617A codeforce
#Description:
#An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

n = int(input())

arr = (5,4,3,2,1)
total = 0
step = 0

for i in arr:
    while total < n:
        total += i
        step += 1

print(step)
