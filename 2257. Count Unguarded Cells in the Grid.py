class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls) -> int:
        guarded = [[0 for N in range(n)] for M in range(m)]
        for guard in guards:
            guarded[guard[0]][guard[1]] = 2
        for wall in walls:
            guarded[wall[0]][wall[1]] = 2
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for guard in guards:
            for direction in directions:
                x, y = guard[0], guard[1]
                i,j = direction[0], direction[1]
                while 0 <= x + i < m and 0 <= y + j < n and guarded[x+i][y+j] < 2:
                    x += i
                    y += j
                    guarded[x][y] = 1
        res = 0
        for M in range(m):
            for N in range(n):
                if guarded[M][N] == 0:
                    res += 1
        return res





        # set_walls = set(walls)
        # guarded = guards + walls
        # for guard in guards:
        #     # right
        #     r = guard[0]
        #     while r < m and [r,guard[1]] not in walls:
        #         if [r,guard[1]] not in guarded:
        #             guarded.append([r,guard[1]])
        #         r += 1
        #         if [r, guard[1]] in guards:
        #             break
        #     # down
        #     c = guard[1]
        #     while c < n and [guard[0],c] not in walls:
        #         if [guard[0],c] not in guarded:
        #             guarded.append([guard[0],c])
        #         c += 1
        #         if [guard[0], c] in guards:
        #             break
        #     # left
        #     rr = guard[0]
        #     while rr >= 0 and [rr, guard[1]] not in walls:
        #         if [rr, guard[1]] not in guarded:
        #             guarded.append([rr, guard[1]])
        #         rr -= 1
        #         if [rr, guard[1]] in guards:
        #             break
        #     # up
        #     rc = guard[1]
        #     while rc >= 0 and [guard[0], rc] not in walls:
        #         if [guard[0], rc] not in guarded:
        #             guarded.append([guard[0], rc])
        #         rc -= 1
        #         if [guard[0], rc] in guards:
        #             break
        # return m*n - len(guarded)


print(Solution().countUnguarded( m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))