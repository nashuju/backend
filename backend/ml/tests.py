#-*- coding: UTF-8 -*-

class Solution():
    def full_package(self,goods,max_V):
        self.goods_remove(goods)
        f = [0] * (max_V + 1)
        for i in range(len(goods)):
            for v in range(max_V+1):
                #特别注意这个ｉｆ语句，如果不写，结果可能会出现错误！！！
                if v>=goods[i][0]:
                    f[v] = max(f[v],f[v-goods[i][0]]+goods[i][1])
        print f
        return f[max_V]

    def goods_remove(self,goods):
        # 操作简化，将所有的不符合条件的good删除
        good_delete = set([])
        for i in range(len(goods)):
            if i in good_delete:
                continue
            for j in range(len(goods)):
                if goods[i][0] <= goods[j][0] and goods[i][1] >= goods[j][1]:
                    if j == i: continue
                    good_delete.add(j)
                elif goods[i][0] >= goods[j][0] and goods[i][1] <= goods[j][1]:
                    if j == i: continue
                    good_delete.add(i)
                else:
                    continue
        good_delete = list(good_delete)
        good_delete.sort(reverse=True)
        for i in good_delete:
            del goods[i]



goods = [[7,1],[3,1],[1,1]]
test = Solution()
print test.full_package(goods,2017)