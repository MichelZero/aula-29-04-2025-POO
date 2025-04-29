# autor: Michel
# data: 2025-04-29

T = ()
B = True
print(type(T))
print(type(B))

T1 = ("1")
print(f"T1 = {type(T1)}")
print(f"T1 = {T1}")

T2 = ("1",)
print(f"T2 = {type(T2)}")
print(f"T2 = {T2}")

print()
T3 = (1,[5, 3], 4)
print(f"T3 = {T3}")

T3[1][0] = 2
print(f"T3 = {T3}")

print()
T4 = (1, 2, 3, 4, 5)
print(f"T4 = {T4}")

print()
R1 = range(5)
T6 = tuple(R1)
print(f"T6 = {type(T6)}")
print(f"T6 = {T6}")