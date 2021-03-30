with open("sorted_values.txt") as file:
    s = file.read()

s = s.split()
s = [float(i) for i in s]
s.sort()

s1, s2 = [], []

for i, v in enumerate(s):
    s1.append(v)
    s2.append(i - 200)

print(len(s1))
print(s1)
print(s2)

step = 30
s1 = tuple(s1[::step])
s2 = tuple(s2[::step])

print(len(s1), len(s2))

print(s1)
print(s2)

assert len(s1) == len(s2)
