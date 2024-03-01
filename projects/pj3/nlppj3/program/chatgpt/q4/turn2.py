
def fibonacci(n):
    if n <= 0:
        raise ValueError("n必须大于0")
    elif n <= 2:
        return 1
    else:
        fib = [0] * n
        fib[0] = 1
        fib[1] = 1
        for i in range(2, n):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n-1]

n = int(input("输入要找到的斐波那契数的位置："))
result = fibonacci(n)
print(f"第{n}个斐波那契数是：{result}")
