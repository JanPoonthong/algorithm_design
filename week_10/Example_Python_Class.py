import copy


class state:
    def __init__(self, n):
        self.a = [-1] * n
        self.b = 0


s = state(20)  # the argument n will be 20
print(len(s.a))  # will print 20
s.a[1] = 23
u = copy.deepcopy(s)
# u = s will create two refs to the same instance
# so must copy in order to create separate instances
u.a[1] = 44  # s.a[1] remains 23
