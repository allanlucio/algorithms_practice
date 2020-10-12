class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        def replace_str_index(text,index=0,replacement=''):
            return '%s%s%s'%(text[:index],replacement,text[index+1:])
        if(len(A) != len(B)): return False
        
        
        diff=0
        index=[]
        for i in range(0, len(A)):
            if(A[i]!=B[i]):
                index.append(i)
                diff+=1
            
            if(diff > 2): return False
        if(diff == 1): return False
        
        if(len(index)==2):
            temp=A
            test=replace_str_index(temp,index[0],A[index[1]])
            test=replace_str_index(test,index[1],A[index[0]])
            
            if(test == B): 
                return True
            else: 
                return False
        else:
            
            if(len(A) > len(set(A))):
                return True
            else:
                return False
            
