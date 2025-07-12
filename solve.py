import re


class HanoiSolver:
    def __init__(self, pegs, disks):
        self.disks = disks
        self.pegs = pegs
        self.moves = []

    def solve(self):
        self.moves.clear()
        if self.pegs == 3:
            self._hanoi(self.disks, 1, 3, 2)
        else:
            pegs_list = list(range(1, len(self.pegs) + 1))
            self._frame_steward(self.disks, pegs_list[0], pegs_list[-1], pegs_list[1:-1])
        print('Début de la résolution')
        print(self.moves)
        return self.moves
    def _min_moves(self, n, pegs):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if pegs == 3:
            return 2 ** n - 1
        return min(2 * self._min_moves(k,pegs) + self._min_moves(n - k, pegs - 1) for k in range(1, n))
    
    def _frame_steward(self, n, source, target, auxiliaries):

        if n == 0:
            return
        
        if n == 1:
            self.moves.append((source, target))
            return
        
        p = len(auxiliaries) + 2

        if p == 3:
            aux = auxiliaries[0]
            self._frame_steward(n - 1, source, aux,[target])
            self.moves.append((source, target))
            self._frame_steward(n - 1, aux, target, [source])
            return
        
        min_moves = float('inf')
        best_k = 1
        for k in range(1, n):
            moves = 2 * self._min_moves(k, p) + self._min_moves(n - k, p - 1)
            if moves < min_moves:
                min_moves = moves
                best_k = k

        aux1 = auxiliaries[0]
        aux2 = auxiliaries[1:]
        self._frame_steward(best_k, source, aux1, aux2 + [target])
        self._frame_steward(n - best_k, source, target, aux2)
        self._frame_steward(best_k, aux1, target, [source] + aux2)

    def _hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.moves.append((source, target))
            print('Dernier disque')
            print(f"Nombre de mouvements: {len(self.moves)}")
            print(f"Nombre de disques: {self.disks}")
            print(f"Nombre de tiges: {self.pegs}")
        else:
            self._hanoi(n-1, source, auxiliary, target)
            self.moves.append((source, target))
            self._hanoi(n-1, auxiliary, target, source)
