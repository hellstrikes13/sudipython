def addi(n):
    if n <=0:
        return 0
    else:
        return (n + addi(n-1))
print addi(5)
