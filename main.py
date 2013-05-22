class UnionFind:
    """ A union-find data structure. """

    def __init__(self, n):
        """ (UnionFind, int) -> NoneType

        The UnionFind initialization with n objects
        """

        self.ids = [x for x in range(n)]

    def root(self, a):
        """ ((UnionFind, int) -> int

        find main root
        """
        while a != self.ids[a]:
            a = self.ids[a]
        return a
    
    def linked(self, p, q):
        """ (UnionFind, int, int) -> bool

        Check connection between p and q
        """

        return self.root(p) == self.root(q)

    def union(self, p, q):
        """ (UnionFind, int, int) -> NoneType

        Add connection between p and q
        """
        
        rp = self.root(p)
        rq = self.root(q)
        self.ids[rp] = rq


if __name__ == '__main__':
    uf = UnionFind(20)
    uf.union(1,2)
