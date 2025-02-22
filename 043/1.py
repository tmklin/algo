import sys
 
Pos = tuple[int, int]
EMPTY = -1
DO_NOTHING = -1
STATION = 0
RAIL_HORIZONTAL = 1
RAIL_VERTICAL = 2
RAIL_LEFT_DOWN = 3
RAIL_LEFT_UP = 4
RAIL_RIGHT_UP = 5
RAIL_RIGHT_DOWN = 6
COST_STATION = 5000
COST_RAIL = 100
 
 
class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1 for _ in range(n * n)]
 
    def _find_root(self, idx: int) -> int:
        if self.parents[idx] < 0:
            return idx
        self.parents[idx] = self._find_root(self.parents[idx])
        return self.parents[idx]
 
    def is_same(self, p: Pos, q: Pos) -> bool:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        return self._find_root(p_idx) == self._find_root(q_idx)
 
    def unite(self, p: Pos, q: Pos) -> None:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        p_root = self._find_root(p_idx)
        q_root = self._find_root(q_idx)
        if p_root != q_root:
            p_size = -self.parents[p_root]
            q_size = -self.parents[q_root]
            if p_size > q_size:
                p_root, q_root = q_root, p_root
            self.parents[q_root] += self.parents[p_root]
            self.parents[p_root] = q_root
 
 
def distance(a: Pos, b: Pos) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
 
 
class Action:
    def __init__(self, type: int, pos: Pos):
        self.type = type
        self.pos = pos
 
    def __str__(self):
        if self.type == DO_NOTHING:
            return "-1"
        else:
            return f"{self.type} {self.pos[0]} {self.pos[1]}"
 
 
class Result:
    def __init__(self, actions: list[Action], score: int):
        self.actions = actions
        self.score = score
 
    def __str__(self):
        return "\n".join(map(str, self.actions))
 
 
class Field:
    def __init__(self, N: int):
        self.N = N
        self.rail = [[EMPTY] * N for _ in range(N)]
        self.uf = UnionFind(N)
 
    def build(self, type: int, r: int, c: int) -> None:
        assert self.rail[r][c] != STATION
        if 1 <= type <= 6:
            assert self.rail[r][c] == EMPTY
        self.rail[r][c] = type
 
        # 隣接する区画と接続
        # 上
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
            if r > 0 and self.rail[r - 1][c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
                self.uf.unite((r, c), (r - 1, c))
        # 下
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
            if r < self.N - 1 and self.rail[r + 1][c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r + 1, c))
        # 左
        if type in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
            if c > 0 and self.rail[r][c - 1] in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r, c - 1))
        # 右
        if type in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
            if c < self.N - 1 and self.rail[r][c + 1] in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
                self.uf.unite((r, c), (r, c + 1))
 
    def is_connected(self, s: Pos, t: Pos) -> bool:
        if distance(s, t) > 4:
            return False
        stations0 = self.collect_stations(s)
        stations1 = self.collect_stations(t)
        for station0 in stations0:
            for station1 in stations1:
                if self.uf.is_same(station0, station1):
                    return True
        return False
 
    def collect_stations(self, pos: Pos) -> list[Pos]:
        stations = []
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if abs(dr) + abs(dc) > 2:
                    continue
                r = pos[0] + dr
                c = pos[1] + dc
                if 0 <= r < self.N and 0 <= c < self.N and self.rail[r][c] == STATION:
                    stations.append((r, c))
        return stations
 
class Solver:
    def __init__(self, N: int, M: int, K: int, T: int, home: list[Pos], workplace: list[Pos]):
        self.N = N
        self.M = M
        self.K = K
        self.T = T
        self.home = home
        self.workplace = workplace
        self.field = Field(N)
        self.money = K
        self.actions = []

    def calc_income(self) -> int:
        income = 0
        for i in range(self.M):
            if self.field.is_connected(self.home[i], self.workplace[i]):
                income += distance(self.home[i], self.workplace[i])
        return income

    def build_station(self, r: int, c: int) -> Pos:
        existing_station = self.find_nearest_station((r, c))
        if existing_station:
            return existing_station

        if not self.can_afford(COST_STATION):
            return (r, c)

        self.field.build(STATION, r, c)
        self.money -= COST_STATION
        self.actions.append(Action(STATION, (r, c)))
        return (r, c)

    def build_rail(self, type: int, r: int, c: int) -> None:
        if not self.can_afford(COST_RAIL):
            return

        self.field.build(type, r, c)
        self.money -= COST_RAIL
        self.actions.append(Action(type, (r, c)))

    def build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
    
    def find_nearest_station(self, pos: Pos) -> Pos | None:
        nearest_station = None
        min_distance = float('inf')

        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if abs(dr) + abs(dc) > 2:
                    continue
                r, c = pos[0] + dr, pos[1] + dc
                if 0 <= r < self.N and 0 <= c < self.N and self.field.rail[r][c] == STATION:
                    d = distance(pos, (r, c))
                    if d < min_distance:
                        min_distance = d
                        nearest_station = (r, c)
        
        return nearest_station

    def find_station_sharing_groups(self) -> list[tuple[list[int], Pos]]:
        station_groups = []
        for r in range(self.N):
            for c in range(self.N):
                shared_passengers = []
                for i in range(self.M):
                    if distance(self.home[i], (r, c)) <= 2 or distance(self.workplace[i], (r, c)) <= 2:
                        shared_passengers.append(i)
                if len(shared_passengers) >= 2:
                    station_groups.append((shared_passengers, (r, c)))
        return station_groups

    def find_longest_distance_pair(self) -> tuple[int, int]:
        max_distance = -1
        best_pair = (-1, -1)
        for i in range(self.M):
            d = distance(self.home[i], self.workplace[i])
            if d > max_distance:
                max_distance = d
                best_pair = (i, i)
        return best_pair
    
    def can_afford(self, cost: int) -> bool:
        return self.money >= cost

    def construct_path(self, s: Pos, t: Pos) -> None:
        r0, c0 = s
        r1, c1 = t

        if r0 < r1:
            for r in range(r0 + 1, r1):
                self.build_rail(RAIL_VERTICAL, r, c0)
            if c0 < c1:
                self.build_rail(RAIL_RIGHT_UP, r1, c0)
            elif c0 > c1:
                self.build_rail(RAIL_LEFT_UP, r1, c0)
        elif r0 > r1:
            for r in range(r0 - 1, r1, -1):
                self.build_rail(RAIL_VERTICAL, r, c0)
            if c0 < c1:
                self.build_rail(RAIL_RIGHT_DOWN, r1, c0)
            elif c0 > c1:
                self.build_rail(RAIL_LEFT_DOWN, r1, c0)

        if c0 < c1:
            for c in range(c0 + 1, c1):
                self.build_rail(RAIL_HORIZONTAL, r1, c)
        elif c0 > c1:
            for c in range(c0 - 1, c1, -1):
                self.build_rail(RAIL_HORIZONTAL, r1, c)

    def solve(self) -> Result:
        station_groups = self.find_station_sharing_groups()
        best_group = None
        best_profit = 0

        for group, station_pos in station_groups:
            shared_count = len(group)
            max_distance = max(distance(self.home[i], self.workplace[i]) for i in group)
            budget_check = (self.money - 10000) // 100 > (self.T - len(self.actions)) * max_distance * shared_count

            if budget_check and shared_count > best_profit:
                best_profit = shared_count
                best_group = (group, station_pos)

        if best_group:
            group, station_pos = best_group
            station_pos = self.build_station(*station_pos)

            for i in group[:2]:
                home_station = self.build_station(*self.home[i])
                self.construct_path(self.home[i], station_pos)
                workplace_station = self.build_station(*self.workplace[i])
                self.construct_path(station_pos, workplace_station)

            income = self.calc_income()
            self.money += income
            while len(self.actions) < self.T:
                self.build_nothing()
                self.money += income
            return Result(self.actions, self.money)

        if self.money >= 17000:
            for group, station_pos in station_groups:
                if len(group) >= 2:
                    first, second = group[:2]
                    station_pos = self.build_station(*station_pos)

                    home_station_first = self.build_station(*self.home[first])
                    self.construct_path(home_station_first, station_pos)
                    workplace_station_first = self.build_station(*self.workplace[first])
                    self.construct_path(station_pos, workplace_station_first)

                    if self.money >= COST_STATION + COST_RAIL * 5:
                        workplace_station_second = self.build_station(*self.workplace[second])
                        self.construct_path(station_pos, workplace_station_second)

                    income = self.calc_income()
                    self.money += income
                    while len(self.actions) < self.T:
                        self.build_nothing()
                        self.money += income
                    return Result(self.actions, self.money)

        i, _ = self.find_longest_distance_pair()
        if i != -1 and (self.money - 10000) // 100 > distance(self.home[i], self.workplace[i]):
            home_station = self.build_station(*self.home[i])
            workplace_station = self.build_station(*self.workplace[i])
            self.construct_path(home_station, workplace_station)

            income = self.calc_income()
            self.money += income
            while len(self.actions) < self.T:
                self.build_nothing()
                self.money += income
            return Result(self.actions, self.money)

        while len(self.actions) < self.T:
            self.build_nothing()

        return Result(self.actions, self.money)

def main():
    N, M, K, T = map(int, input().split())
    home = []
    workplace = []
    for _ in range(M):
        r0, c0, r1, c1 = map(int, input().split())
        home.append((r0, c0))
        workplace.append((r1, c1))
 
    solver = Solver(N, M, K, T, home, workplace)
    result = solver.solve()
    print(result)
    #print(f"score={result.score}", file=sys.stderr)
 
if __name__ == "__main__":
    main()