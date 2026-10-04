class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #we have two separate lists all referring to a car at the same position, so we can zip tgt. Also want to sort in descending order so we have the cars closest to the finish line accounted for first, any behind cars that catch up and take equal or less time can be counted in that fleet too. If the cars behind take longer to finish, fleet += 1
        cars = sorted(zip(position, speed), reverse = True)
        res = 0
        currMaxTime = 0
        for pos, speed in cars:
            #x = vt
            time = (target-pos) / speed
            if time > currMaxTime:
                res += 1
                currMaxTime = time
        return res