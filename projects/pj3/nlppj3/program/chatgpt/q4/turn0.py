
def fibonacci(n):
    if n <= 0:
        return "n必须大于0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]  # 用数组存储斐波那契数列
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[-1]

n = int(input("请输入n的值："))
print("第", n, "个斐波那契数是：", fibonacci(n))
