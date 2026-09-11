def find_dup_str(s, n):
    if n > len(s):
        return ""
 
    i = 0
    while i <= len(s) - n:
        candidate = s[i:i+n]
 
        j = i + n  #starts looking so pieces don't overlap
        while j <= len(s) - n:
            piece = s[j:j+n]
            if candidate == piece:
                return candidate
            j += 1
 
        i += 1
 
    return ""
 
 
#finds the longest substring that's duplicated
def find_max_dup(s):
    best = ""
 
    n = 1
    while n <= len(s):
        found = find_dup_str(s, n)
        if found == "":
            break  #if this length has no duplicate, longer ones won't either
        best = found
        n += 1
 
    return best
 
 
s = input("Enter a string:")
n = int(input("Enter a length: "))
print(find_dup_str(s, n))
 
s2 = input("Enter a string to find the longest duplicate in: ")
print(find_max_dup(s2))