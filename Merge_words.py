#Program takes two words word1 and word2 and alternatively combines their characters
def mergeAlternately(word1, word2):
    ans = []
    if len(word1) == len(word2):
        for i in range(len(word1)):
            ans.append(word1[i]+word2[i])
        x = "".join(ans)
        return x
    else: 
        
        z = len(word1)
        q = len(word2)
        if z > q:
            h = word1
        else:
            h = word2
        m = min(z, q)
        for i in range(m):
            ans.append(word1[i]+word2[i])
        x = "".join(ans)
        l = len(h)
        final = x + h[l-2:]
        return final