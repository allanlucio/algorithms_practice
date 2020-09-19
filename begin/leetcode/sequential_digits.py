class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        i=1
        temp=i+1
        valor=1
        lista=[]
        while(True):
            
            valor = valor * 10 + temp
            # print(valor)
            if(i > 8):break
            
            elif(valor>=low and valor <= high and temp<=9):
                lista.append(valor)
            
            if(valor>high): 
                i+=1
                temp=i+1
                valor=i
            else:
                temp+=1
            
            
            
            
    
        lista.sort()
        return lista
