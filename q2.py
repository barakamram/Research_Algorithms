def four_neighbor_function(node):
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def breadth_first_search(start, end, neighbor_function):
    visited, queue = [start], [[start]]  # the queue is a list of lists
    while queue:
        m = queue.pop(0)  # the first list in the queue
        if m[-1] == end:  # find the wey to the end
            return m
        for nei in neighbor_function(m[-1]):
            trail = list(m)  # to save the trail
            if nei not in visited:
                visited.append(nei)  # add nei to visited
                trail.append(nei)  # add nei to the trail
                queue.append(trail)  # save the trail


if __name__ == "__main__":
    print('(0,0) -> (2,2) ----->', breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
    # [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    print('(2,-1) -> (-3,5) ----->', breadth_first_search(start=(2, -1), end=(-3, 5), neighbor_function=four_neighbor_function))
    # [(2, -1), (1, -1), (0, -1), (-1, -1), (-2, -1), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5)]
