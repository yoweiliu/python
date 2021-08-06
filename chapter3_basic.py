"""
# 數字介紹
"""
# 把 Python 當作計算機使用
print(17 / 3)  # classic division returns a float
print(17 // 3)  # floor division discards the fractional part
print(17 % 3)  # the % operator returns the remainder of the division
print(5 * 3 + 2)  # floored quotient * divisor + remainder
print(5 ** 2)   # 5 squared

# 浮點數的運算有完善的支援
print(4 * 3.75 - 1)  # 運算子(operator)遇上混合的運算元(operand)時，會把整數的運算元轉換為浮點數：


"""
# 字串介紹
"""
# 單引號 ('...') 或雙引號 ("...") 之中，兩者會得到相同的結果
print('"Yes," they said.')
print("\"Yes,\" they said.")

# 如果你不希望字元前出現 \ 就被當成特殊字元時，可以改使用 raw string，在第一個包圍引號前加上 r ：
print('C:\some\name')
print(r'C:\some\name')

# 字串可以被「索引 indexed」(下標，即 subscripted)，
# 第一個字元的索引值為 0。沒有獨立表示字元的型別；一個字元就是一個大小為 1 的字串：
word = 'Python'
print(word[0])  # character in position 0
# 'P'
print(word[-1])  # last character
# 'n'

print()
# 除了索引外，字串亦支援「切片 slicing」。索引用來拿到單獨的字元，而切片則可以讓你拿到子字串 (substring)：
print(word[0:2])    # characters from position 0 (included) to 2 (excluded)
# 'Py'
# 注意到起點永遠被包含，而結尾永遠不被包含。這確保了 s[:i] + s[i:] 永遠等於 s：
print(word[:2] + word[2:])
# 'Python'

# 切片索引 (slice indices) 有很常用的預設值，
# 省略起點索引值時預設為 0，而省略第二個索引值時預設整個字串被包含在 slice 中：
print(word[-2:])    # characters from the second-last (included) to the end
# 'on'
