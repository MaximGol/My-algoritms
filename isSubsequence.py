def isSubsequence(s, t) -> bool:
        for i in s:
            if i in t:
                t =t[t.find(i)+1:]
            else:
                return False
        return True

s ="aaaaaa"
t ="bbaaaa"
a = isSubsequence(s,t)
print (a)