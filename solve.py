# Algorithme récursif de résolution

class HanoiSolver:
    def __init__(self, disks: int, pegs: int = 3):
        self.disks = disks
        self.pegs = pegs
        self.moves = []

    def solve(self):
        if self.pegs != 3:
            raise NotImplementedError("La version avec plus de 3 tiges n’est pas encore implémentée.")
        self._hanoi(self.disks, 1, 3, 2)
        return self.moves

    def _hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.moves.append((source, target))
        else:
            self._hanoi(n-1, source, auxiliary, target)
            self.moves.append((source, target))
            self._hanoi(n-1, auxiliary, target, source)
