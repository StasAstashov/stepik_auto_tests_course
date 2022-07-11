class Sortir:
 def sortirovka(a):
    a = a.copy()
    N = len(a)
    for i in range(N-1):
     for j in range (N-1-i):
          if a[j] > a[j+1]: 
             a[j], a[j+1] = a[j+1], a[j]
    return a

b = [1,9,7,5,3]
print(Sortir.sortirovka(b))