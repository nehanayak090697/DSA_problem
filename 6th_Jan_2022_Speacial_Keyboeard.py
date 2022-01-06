#User function Template for python3
arr=[0]*75
def length(n):
  m=0
  if n<7:
    return n
  r=0
  for b in range(n-3,1,-1):
    if arr[b]>0:
        r=(n-1-b)*arr[b]
    else:
        x=length(b)
        arr[b]=x
        r = (n-1-b)*arr[b]
    if r>m:
      m=r
  return m
N=int(input())
print(length(n))
