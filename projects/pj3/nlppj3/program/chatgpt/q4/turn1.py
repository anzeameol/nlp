
def fibonacci(n):
    # 初始化斐波那契数列的前两个数
    fib = [0, 1]

    # 计算第n个斐波那契数
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    # 返回第n个斐波那契数
    return fib[n]

# 测试程序
n = int(input("请输入一个整数n："))
result = fibonacci(n)
print("第{}个斐波那契数是：{}".format(n, result))
