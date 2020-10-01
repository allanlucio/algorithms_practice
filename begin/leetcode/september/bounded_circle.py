class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        

        direction=0
        coord = [0,0]

        for ins in instructions:
            if(ins == 'L'):
                direction = (direction-1) % 4
            elif(ins == 'R'):
                direction = (direction+1) % 4
            else:
                if(direction == 0):
                    coord[1]+=1
                elif(direction == 2):
                    coord[1]-=1
                elif(direction == 1):
                    coord[0]-=1
                elif(direction == 3):
                    coord[0]+=1

            
        if(coord[0]==0 and coord[1]==0):
            return True
        elif(direction==0 and len(instructions)!=0):
            return False
        else:
            return True
        