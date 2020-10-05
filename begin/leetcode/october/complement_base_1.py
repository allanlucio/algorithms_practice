class Solution:
    def bitwiseComplement(self, N: int) -> int:
        value = N
        if(N==0) : return 1
        result=""
        while value >= 1:
            if(value%2 == 0):
                result="0"+result
            else:
                result = "1"+result
            value//=2
        
        result2=""
        for a in result:
            if(a=="0"):
                result2= result2+"1"
            else:
                result2= result2+"0"
        
        
        result=result2[::-1]
        index = 0 
        value=0
        for e in result:
            if(e=="1"):
                value += 2**index
                
            index+=1
        
        return value
