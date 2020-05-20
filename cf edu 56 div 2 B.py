print('\n'.join([(lambda s : '-1' if sorted(s)[0] == sorted(s)[-1] else ''.join(sorted(s)))(input()) for i in range(int(input()))]))
