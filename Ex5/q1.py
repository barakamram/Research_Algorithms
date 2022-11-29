import doctest
import copy

class bounded_subsets:
    '''
    >>> for s in bounded_subsets([1,2,3], 4): print(s, end=',')
    [],[1],[2],[3],[1, 2],[1, 3],
    >>> for s in bounded_subsets(range(50,150), 103): print(s, end=',')
    [],[50],[51],[52],[53],[54],[55],[56],[57],[58],[59],[60],[61],[62],[63],[64],[65],[66],[67],[68],[69],[70],[71],[72],[73],[74],[75],[76],[77],[78],[79],[80],[81],[82],[83],[84],[85],[86],[87],[88],[89],[90],[91],[92],[93],[94],[95],[96],[97],[98],[99],[100],[101],[102],[103],[50, 51],[50, 52],[50, 53],[51, 52],
    >>> for s in bounded_subsets([1, 5, 2, 3, 4], 3):  print(s, end=',')
    [],[1],[2],[3],[1, 2],
    >>> for s in bounded_subsets([5, 1, 2, 3, 4], 6): print(s, end=',')
    [],[5],[1],[2],[3],[4],[1, 5],[1, 2],[1, 3],[1, 4],[2, 3],[2, 4],[1, 2, 3],
    >>> for s in bounded_subsets(range(10,30), 25): print(s, end=',')
    [],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],[25],[10, 11],[10, 12],[10, 13],[10, 14],[10, 15],[11, 12],[11, 13],[11, 14],[12, 13],
    '''

    def __init__(self, s: list, c: int):
        self.s = s
        self.limit = c
        self.subsets = list(list())
        self.subsets.append([])
        for x in s:
            if x <= c:
                self.subsets.append([x])
        self.keep_digging(self.subsets)
        self.max = len(self.subsets)  # the max of the legal subset
        self.curr = -1  # the current element in subset

    def __iter__(self):
        return self

    def __next__(self):
        self.curr += 1
        if self.curr < self.max:
            return self.subsets[self.curr]
        raise StopIteration

    def keep_digging(self, s: list):
        curr_ss = []
        for ss in s:
            css = sum(ss)
            if self.limit <= css:  # css bigger then limit
                continue
            for x in self.s:
                if (css + x) <= self.limit and x not in ss:  # there are no duplicates
                    nss = copy.deepcopy(ss)  # deep copy
                    nss.append(x)
                    nss.sort()  # there are no duplicates (x, y) == (y, x)
                    if nss not in self.subsets:
                        curr_ss.append(nss)
                        self.subsets.append(nss)
        if len(curr_ss) != 0:
            self.keep_digging(curr_ss)  # recursion


if __name__ == '__main__':
    print(doctest.testmod())
    for s in bounded_subsets([1, 5, 2, 3, 4], 3):
        print(s, end=' ')
    print('\n')
    for s in bounded_subsets([5, 1, 2, 3, 4], 6):
        print(s, end=' ')
