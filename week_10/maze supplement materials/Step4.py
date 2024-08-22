Adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# For a position (r, c), the four positions around it can be computed by
#
# for relativePos in Adj:
#    adjacentPos = (r + relativePos[0], c + relativePos[1])
#
# Then, adjacentPos can be checked whether it is a valid problem state.
