def pow2(n):
    pow=1
    for i in range(n):
        pow=i*i      # pow1   1*2
        yield pow
for v in pow2(8):
    print(v)