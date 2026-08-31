class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = [(target-pair[0][0])/pair[0][1]]
        fleets = 1
        for pos, speed in pair:
            time = (target - pos)/speed
            if time <= stack[0]:
                continue
            else:
                stack.pop()
                stack.append(time)
                fleets += 1
        return fleets