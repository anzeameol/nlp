
def fibonacci(n):
    if n <= 0:
        return "输入错误，请输入正整数"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

n = int(input("请输入一个正整数: "))
print(fibonacci(n))
