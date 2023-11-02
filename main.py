# 1 задание
#def all_divisors(num):
    #devis = []
    #for i in range(1, int(num ** 0.5) + 1):
        #if num % i == 0:
            #devis.append(i)
            #if i != num // i:
               # devis.append(num // i)
    #devis.sort()
    #return devis
#num = [23436, 190187200, 380457890232]
#for num in num:
    #devis = all_divisors(num)
    #print(f"Делители числа {num}: {devis}")


# 2 задание
#def three_args(*, num_1=None, num_2=None, num_3=None):
    #args = []
   # if num_1 is not None:
        #args.append(f"var1 = {num_1}")
    #if num_2 is not None:
       # args.append(f"var2 = {num_2}")
    #if num_3 is not None:
       # args.append(f"var3 = {num_3}")
    #if args:
        #print("Переданы аргументы:", ", ".join(args))
    #else:
       # print("Аргументы не были переданы.")

#three_args(num_1 = 2, num_3 = 10)
#three_args(num_2 = "Hello")
#three_args(num_3 = 5, num_1=None, num_2 = None)


# 3 задание
#def is_palindrome(x):
    #x = x.replace(" ", "").lower()
    #return x == x[::-1]

#print(is_palindrome("racecar"))
#print(is_palindrome("hello"))
#print(is_palindrome("A man a plan a canal Panama"))


# 4 задание
#def most_common_and_longest_words(text):
    #x = text.lower().split()
    #x = [word.strip(".,!?") for word in x]
    #word_counts = {}
    #for word in x:
        #if word:
            #if word in word_counts:
                #word_counts[word] += 1
            #else:
               # word_counts[word] = 1

    #most_common_word = max(word_counts, key=word_counts.get)
    #longest_word = max(x, key=len)
    #return most_common_word, longest_word


#text = input("Введите текст: ")
#most_common, longest = most_common_and_longest_words(text)
#print(f"Наиболее часто встречающееся слово: {most_common}")
#print(f"Самое длинное слово: {longest}")


# 5 задание
#def generate_spiral_matrix(n, m):
    #chis = [[0] * m for _ in range(n)]
    #num = 1
    #top, bottom, left, right = 0, n - 1, 0, m - 1

    #while num <= n * m:
        #for i in range(left, right + 1):
            #chis[top][i] = num
            #num += 1
       # top += 1
        #for i in range(top, bottom + 1):
            #chis[i][right] = num
            #num += 1
        #right -= 1
        #for i in range(right, left - 1, -1):
            #chis[bottom][i] = num
            #num += 1
        #bottom -= 1
        #for i in range(bottom, top - 1, -1):
            #chis[i][left] = num
           # num += 1
       # left += 1
   # return chis

#x = int(input("Введите количество строк: "))
#y = int(input("Введите количество столбцов: "))
#spiral_matrix = generate_spiral_matrix(x, y)

#for row in spiral_matrix:
   #for num in row:
        #print(num, end="\t")
    #print()

# 6 задание

def is_magic_square(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != expected_sum:
            return False
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != expected_sum:
            return False
    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False
    if sum(matrix[i][n - i - 1] for i in range(n)) != expected_sum:
        return False

    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")