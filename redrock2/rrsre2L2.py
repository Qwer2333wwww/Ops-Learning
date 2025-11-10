def gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def loop(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print("\n生成器：")
#a=0
# for num in gen(1000000):
for num in gen(10):
    # a+=1
    print(num, end=" ")
# print("Done!")

print("\n普通循环：")
# f_list = loop(1000000)
f_list = loop(10)
# print("Done!")
print(f_list)

#按理说生成器是流式处理，性能更优
#普通循环用时为生成器的接近4.5倍
#但是还是没太懂迭代器和生成器
#完蛋