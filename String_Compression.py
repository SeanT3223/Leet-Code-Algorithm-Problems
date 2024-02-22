class Solution(object):
    def compress(self, chars):
        s= []
        counter = 1
        for i in range(len(chars)):
            if len(chars) == 1:
                s.append(chars[i])
            elif len(chars)-1 == i:
                s.append(chars[i])
                s.append(counter)
            else:
                if chars[i] != chars[i+1] and counter == 1 :
                    s.append(chars[i])
                elif chars[i] == chars[i+1]:
                    counter += 1
                elif chars[i] !=  chars[i+1] and counter > 1:
                    s.append(chars[i])
                    s.append(counter)
                    counter = 1
                elif chars[i] != chars[i+1] and counter == 1:
                    s.append(chars[i])
        chars = s
        return chars
                
            

