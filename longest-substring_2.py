# Given a string, find the length of the longest substring without repeating characters.
# input: 'abrkaabcdefghijjxxx'
# output: 'abcdefghij', 10
# input: 'microsoft'
# output: 'micros', 6

input= 'abrkaabcdefghijjxxx'
y = {}
for i in range(len(input)):
    counter = 0
    a = ""
    for i in range(len(input)):
        if input[counter] not in a:
            a = a + input[counter]
            counter += 1
    y[a] = len(a)
    input = input[len(a):]
b = max(y.keys(), key= lambda k: y[k])
print(b, len(b))