class ThreeElements:
    def __init__(self, ls):
        self.ls = ls


    def find(self):
        result = []
        n = len(self.ls)

        for i in range(n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if self.ls[i] + self.ls[j] + self.ls[k] == 0:
                        result.append([self.ls[i], self.ls[j], self.ls[k]])

        return result

ls = [-25,-10,-7,-3,2,4,8,10]
new_list = ThreeElements(ls)
print(new_list.find())
