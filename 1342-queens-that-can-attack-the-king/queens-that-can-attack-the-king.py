class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set()

        for queen in queens:
            queen_set.add((queen[0],queen[1]))

        direction = [
            (-1,0),
            (0,1),
            (0,-1),
            (1,0),
            (-1,1),
            (-1,-1),
            (1,1),
            (1,-1)
        ]

        result = []

        for dx,dy in direction:
            x = king[0]
            y = king[1]

            while True:
                x += dx
                y += dy

                if x < 0 or x >= 8 or y < 0 or y >= 8:
                    break

                if (x,y) in queen_set:
                    result.append([x,y])
                    break
        return result