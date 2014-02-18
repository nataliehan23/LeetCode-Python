def wordBreak(s, dict):
    if len(s) == 0:
        return False
    ss = len(s)

    print "string length is:", ss

    mp = [[False for i in range(ss)] for j in range(ss)]
    print mp

    for i in range(ss):
        for j in range(i, ss):
            print "i",i
            print "j", j
            print s[i:j+1]
            if s[i:j+1] in dict:
                    mp[i][j] = True

    print mp

    for i in range(ss):
        for j in range(i, ss):
            for k in range(i, j):
                if mp[i][j]==False:
                    mp[i][j] = mp[i][k] and mp[k+1][j]
    print mp
    
    return mp[0][ss-1]

s = "cars"
dict = ["car","ca","rs"]
print wordBreak(s, dict)
