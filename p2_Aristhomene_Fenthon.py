def find_Pythagorean(n):
    triples = []
 
 #tries every possible combo from 1 to n
    a = 1
    while a <= n:
        b = 1
        while b <= n:
            c = 1
            while c <= n:
                #checks if the numbers form a right triangle
                if a**2 + b**2 == c**2:
                    triples.append((a, b, c))
                c += 1
            b += 1
        a += 1
 
    return triples
 
 
n = int(input("Enter n:"))
result = find_Pythagorean(n)
for triple in result:9
print(triple)