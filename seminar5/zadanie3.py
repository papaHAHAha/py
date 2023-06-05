def simpleNumber(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return(f"number {n} is simple")
    else:
        return(f"number {n} is not simple")
print(simpleNumber(10))
