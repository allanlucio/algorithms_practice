class Solution:
    chosen=[]
    def find_candidates(self,idx, target,act,candidates):
        if(target == 0):
            self.chosen.append(act)
            
        index=idx
        for elemento in candidates[idx:]:
            
            if(elemento<=target):
                v=act.copy()
                v.append(elemento)
                self.find_candidates(index,target-elemento,v,candidates)
            index+=1
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.chosen=[]
        self.find_candidates(0,target,[],candidates)
        
        return self.chosen
