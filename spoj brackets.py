from sys import stdin,stdout
ok = [1]

def init(node,left,right,brackets,cnt):
    if  left == right:
        cnt.setdefault(node,0)
        if brackets[left] == '(':
            cnt[node] += 1
        else:
            cnt[node] -= 1
        return 0      
    mid,l,r = (left + right) >> 1, node<<1 , (node<<1) + 1
    init(l, left, mid, brackets, cnt)
    init(r, mid+1, right, brackets, cnt)
    cnt.setdefault(node,0)
    cnt[node] = cnt[l] + cnt[r]
    if l == 2 and cnt[node] == 0:
        if cnt[l] < cnt[r]:
            ok[0] = 0

def update(node,left,right,i,brackets,cnt):
    if left > i or right < i:
        return 0
    if  left == right:
        brackets[i] = '(' if brackets[i] == ')' else ')'
        cnt[node] = 1 if brackets[i] == '(' else -1
        return 0
    mid,l,r = (left + right) >> 1, node<<1 , (node<<1) + 1
    update(l, left, mid, i, brackets, cnt)
    update(r, mid+1, right, i, brackets, cnt)
    cnt[node] = cnt[l] + cnt[r]
    if l == 2 and cnt[node] == 0:
        if cnt[l] < cnt[r]:
            ok[0] = 0
    
def main():
    for i in range(1,11):
        n = int(stdin.readline())
        brackets = list(stdin.readline())
        brackets.pop()
        cnt,output,ok[0] = dict(),['Test '+str(i)+':'], 1
        if n%2 == 0:
            init(1,0,n-1,brackets,cnt)
        m = int(stdin.readline())
        while m:
            m -= 1
            q = int(stdin.readline())
            if q == 0:
                output.append('NO' if n%2 or cnt[1] or not ok[0]  else 'YES')
            elif n%2 == 0:
                ok[0] = 1
                update(1,0,n-1,q-1,brackets,cnt)
        stdout.write('\n'.join(output))
        stdout.write('\n')

main()






















