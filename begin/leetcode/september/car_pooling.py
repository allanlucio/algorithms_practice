class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        num_passenger_passengers = []        
        for index in range(0,1000):
            num_passenger_passengers.append(0)
            
        for location in trips:
            
            num_passenger_passengers[location[1]]+=location[0]
            num_passenger_passengers[location[2]]-=location[0]
            
        current_number=0
        for point in num_passenger_passengers:
            current_number+=point
            
            if(current_number > capacity):
                return False
            
        
        return True
