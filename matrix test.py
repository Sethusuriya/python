s=[[5, 1, 4],
   [4, 4, 2] ,
   [1, 2, 7]]
p=[[7, 2, 1 ] ,
   [5, 2, 3],
   [6, 2, 2]]
add=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range (len(s)):
    for j in range(len(s[0])):
        add[i][j]=s[i][j]+p[i][j]
for r in add:
     print(r)
