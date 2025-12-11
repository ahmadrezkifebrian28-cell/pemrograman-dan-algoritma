stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

# pop
stack.pop()



size = 10
arr = [None] * size

top1 = -1
top2 = size

# push stack 1
top1 += 1
arr[top1] = 100

# push stack 2
top2 -= 1
arr[top2] = 200

print(arr)  #single
print(stack)  #  double
