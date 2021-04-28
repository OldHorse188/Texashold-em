from model.JudgeInfo import JudgeInfo

# 用户类


class User:
    __slots__ = ("__uid", "__name", "__pokers", "__money")

    def __init__(self, uid, name, money):
        self.__uid = uid
        self.__name = name
        self.__pokers = []
        self.__money = money

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, uid):
        self.__uid = uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pokers(self):
        return self.__pokers

    @pokers.setter
    def pokers(self, pokers):
        self.__pokers = pokers
        # 整理手牌
        self.__pokers.sort(reverse=True)

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def add_money(self, add_num):
        self.__money += add_num

    def sub_money(self, sub_num):
        self.__money -= sub_num

    @staticmethod
    def is_same_color(poker_list):
        # 是否为 同花色序列
        for p in poker_list:
            if p.color != poker_list[0].color:
                return False
        return True

    @staticmethod
    def is_arithmetic(poker_list, incr):
        # 是否为 公差为incr 的 等差递增序列
        inc = 0
        for p in poker_list:
            if p.num != poker_list[0].num - inc:
                return False
            inc += incr
        return True

    def is_royal_straight_flush(self):
        # 大同花顺
        if self.is_same_color(self.__pokers) and self.is_arithmetic(self.__pokers, 1) and self.__pokers[0].num == 14:
            return JudgeInfo(10, self.__pokers)
        else:
            return False

    def is_straight_flush(self):
        # 同花顺
        if self.is_same_color(self.__pokers) and self.is_arithmetic(self.__pokers, 1):
            return JudgeInfo(9, self.__pokers)
        else:
            return False

    def is_four_of_a_kind(self):
        # 四条
        pokers_list = []
        if self.is_arithmetic(self.__pokers[0: 4], 0):
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(8, pokers_list)
        elif self.is_arithmetic(self.__pokers[1: 5], 0):
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[0])
            return JudgeInfo(8, pokers_list)
        else:
            return False

    def is_full_house(self):
        # 满堂红
        pokers_list = []
        # x x x y y
        if self.is_arithmetic(self.__pokers[0: 3], 0) and self.__pokers[3].num == self.__pokers[4].num:
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[3])
            return JudgeInfo(7, pokers_list)
        # x x y y y
        elif self.is_arithmetic(self.__pokers[2: 5], 0) and self.__pokers[0].num == self.__pokers[1].num:
            pokers_list.append(self.__pokers[2])
            pokers_list.append(self.__pokers[0])
            return JudgeInfo(7, pokers_list)
        else:
            return False

    def is_flush(self):
        # 同花
        if self.is_same_color(self.__pokers):
            return JudgeInfo(6, self.__pokers)
        else:
            return False

    def is_straight(self):
        # 顺子
        if self.is_arithmetic(self.__pokers, 1):
            return JudgeInfo(5, self.__pokers)
        else:
            return False

    def is_three_of_a_kind(self):
        # 三条
        pokers_list = []
        # x x x y z
        if self.is_arithmetic(self.__pokers[0: 3], 0) and self.__pokers[3].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(4, pokers_list)
        # x y y y z
        elif self.is_arithmetic(self.__pokers[1: 4], 0) and self.__pokers[0].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(4, pokers_list)
        # x y z z z
        elif self.is_arithmetic(self.__pokers[2: 5], 0) and self.__pokers[0].num != self.__pokers[1].num:
            pokers_list.append(self.__pokers[2])
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[1])
            return JudgeInfo(4, pokers_list)
        else:
            return False

    def is_two_pair(self):
        # 两对
        pokers_list = []
        # x x y y z
        if self.__pokers[0].num == self.__pokers[1].num and \
                self.__pokers[2].num == self.__pokers[3].num and \
                self.__pokers[1].num != self.__pokers[2].num and \
                self.__pokers[3].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[2])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(3, pokers_list)
        # x x y z z
        elif self.__pokers[0].num == self.__pokers[1].num and \
                self.__pokers[3].num == self.__pokers[4].num and \
                self.__pokers[1].num != self.__pokers[2].num and \
                self.__pokers[2].num != self.__pokers[3].num:
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[2])
            return JudgeInfo(3, pokers_list)
        # x y y z z
        elif self.__pokers[1].num == self.__pokers[2].num and \
                self.__pokers[3].num == self.__pokers[4].num and \
                self.__pokers[0].num != self.__pokers[1].num and \
                self.__pokers[2].num != self.__pokers[3].num:
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[0])
            return JudgeInfo(3, pokers_list)
        else:
            return False

    def is_one_pair(self):
        # 一对
        pokers_list = []
        if self.__pokers[0].num == self.__pokers[1].num and \
                self.__pokers[1].num != self.__pokers[2].num and \
                self.__pokers[2].num != self.__pokers[3].num and \
                self.__pokers[3].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[2])
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(2, pokers_list)
        elif self.__pokers[0].num != self.__pokers[1].num and \
                self.__pokers[1].num == self.__pokers[2].num and \
                self.__pokers[2].num != self.__pokers[3].num and \
                self.__pokers[3].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(2, pokers_list)
        elif self.__pokers[0].num != self.__pokers[1].num and \
                self.__pokers[1].num != self.__pokers[2].num and \
                self.__pokers[2].num == self.__pokers[3].num and \
                self.__pokers[3].num != self.__pokers[4].num:
            pokers_list.append(self.__pokers[2])
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[4])
            return JudgeInfo(2, pokers_list)
        elif self.__pokers[0].num != self.__pokers[1].num and \
                self.__pokers[1].num != self.__pokers[2].num and \
                self.__pokers[2].num != self.__pokers[3].num and \
                self.__pokers[3].num == self.__pokers[4].num:
            pokers_list.append(self.__pokers[3])
            pokers_list.append(self.__pokers[0])
            pokers_list.append(self.__pokers[1])
            pokers_list.append(self.__pokers[2])
            return JudgeInfo(2, pokers_list)
        else:
            return False

    def get_pokers_info(self):
        if self.is_royal_straight_flush():
            j_type = "大同花顺"
            j_info = self.is_royal_straight_flush()
        elif self.is_straight_flush():
            j_type = "同花顺"
            j_info = self.is_straight_flush()
        elif self.is_four_of_a_kind():
            j_type = "四条"
            j_info = self.is_four_of_a_kind()
        elif self.is_full_house():
            j_type = "满堂红"
            j_info = self.is_full_house()
        elif self.is_flush():
            j_type = "同花"
            j_info = self.is_flush()
        elif self.is_straight():
            j_type = "顺子"
            j_info = self.is_straight()
        elif self.is_three_of_a_kind():
            j_type = "三条"
            j_info = self.is_three_of_a_kind()
        elif self.is_two_pair():
            j_type = "两对"
            j_info = self.is_two_pair()
        elif self.is_one_pair():
            j_type = "一对"
            j_info = self.is_one_pair()
        else:
            j_type = "散牌"
            j_info = JudgeInfo(1, self.__pokers)
        return j_type, j_info
