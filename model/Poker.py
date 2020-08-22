import random

from model.JudgeInfo import JudgeInfo


class Poker:
    __slots__ = ("__color", "__num")

    def __init__(self, color, num):
        # 花色 ♠=4 ♥=3 ♣=2 ♦=1
        self.__color = color
        # 大小 2-14
        self.__num = num

    def __repr__(self):
        if self.__color == 1:
            v_color = "♦"
        elif self.__color == 2:
            v_color = "♣"
        elif self.__color == 3:
            v_color = "♥"
        elif self.__color == 4:
            v_color = "♠"
        else:
            v_color = "ERROR"

        if self.__num == 11:
            v_num = "J"
        elif self.__num == 12:
            v_num = "Q"
        elif self.__num == 13:
            v_num = "K"
        elif self.__num == 14:
            v_num = "A"
        elif 2 <= self.__num <= 14:
            v_num = str(self.__num)
        else:
            v_num = "ERROR"

        return v_color + " " + v_num

    def __lt__(self, other):
        # 定义 < 运算
        if self.__num < other.num:
            return True
        elif self.__num == other.num:
            if self.__color < other.color:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        # 定义 == 运算
        if self.__num == other.num and self.__color == other.color:
            return True
        else:
            return False

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @staticmethod
    def sort_pokers(poker_list):
        # 排序：整理手牌
        poker_list.sort(reverse=True)
        return poker_list

    @staticmethod
    def shuffle_pokers():
        # 洗牌
        poker_list = []
        for color in range(1, 5):
            for num in range(2, 15):
                poker_list.append(Poker(color, num))
        random.shuffle(poker_list)
        return poker_list

    @staticmethod
    def deal_pokers(poker_list, deal_num):
        # 发牌
        pokers = []
        if len(poker_list) < 5:
            pokers.append("牌已发完，游戏结束")
        else:
            for pa in range(0, deal_num):
                pokers.append(poker_list.pop(0))
        return pokers

    @staticmethod
    def is_same_color(sorted_pokers):
        # 是否为 同花色序列
        for p in sorted_pokers:
            if p.color != sorted_pokers[0].color:
                return False
        return True

    @staticmethod
    def is_arithmetic(sorted_pokers, incr):
        # 是否为 公差为incr 的 等差递增序列
        inc = 0
        for p in sorted_pokers:
            if p.num != sorted_pokers[0].num - inc:
                return False
            inc += incr
        return True

    @staticmethod
    def is_royal_straight_flush(sorted_pokers):
        # 大同花顺
        if Poker.is_same_color(sorted_pokers) and sorted_pokers[0].num == 14 and Poker.is_arithmetic(sorted_pokers, 1):
            return JudgeInfo(10, sorted_pokers)
        else:
            return False

    @staticmethod
    def is_straight_flush(sorted_pokers):
        # 同花顺
        if Poker.is_same_color(sorted_pokers) and Poker.is_arithmetic(sorted_pokers, 1):
            return JudgeInfo(9, sorted_pokers)
        else:
            return False
        pass

    @staticmethod
    def is_four_of_a_kind(sorted_pokers):
        # 四条
        pokers_list = []
        if Poker.is_arithmetic(sorted_pokers[0: 4], 0):
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(8, pokers_list)
        elif Poker.is_arithmetic(sorted_pokers[1: 5], 0):
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[0])
            return JudgeInfo(8, pokers_list)
        else:
            return False

    @staticmethod
    def is_full_house(sorted_pokers):
        # 满堂红
        pokers_list = []
        # x x x y y
        if Poker.is_arithmetic(sorted_pokers[0: 3], 0) and sorted_pokers[3].num == sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[3])
            return JudgeInfo(7, pokers_list)
        # x x y y y
        elif Poker.is_arithmetic(sorted_pokers[2: 5], 0) and sorted_pokers[0].num == sorted_pokers[1].num:
            pokers_list.append(sorted_pokers[2])
            pokers_list.append(sorted_pokers[0])
            return JudgeInfo(7, pokers_list)
        else:
            return False

    @staticmethod
    def is_flush(sorted_pokers):
        # 同花
        if Poker.is_same_color(sorted_pokers):
            return JudgeInfo(6, sorted_pokers)
        else:
            return False

    @staticmethod
    def is_straight(sorted_pokers):
        # 顺子
        if Poker.is_arithmetic(sorted_pokers, 1):
            return JudgeInfo(5, sorted_pokers)
        else:
            return False

    @staticmethod
    def is_three_of_a_kind(sorted_pokers):
        # 三条
        pokers_list = []
        # x x x y z
        if Poker.is_arithmetic(sorted_pokers[0: 3], 0) and sorted_pokers[3].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(4, pokers_list)
        # x y y y z
        elif Poker.is_arithmetic(sorted_pokers[1: 4], 0) and sorted_pokers[0].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(4, pokers_list)
        # x y z z z
        elif Poker.is_arithmetic(sorted_pokers[2: 5], 0) and sorted_pokers[0].num != sorted_pokers[1].num:
            pokers_list.append(sorted_pokers[2])
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[1])
            return JudgeInfo(4, pokers_list)
        else:
            return False

    @staticmethod
    def is_two_pair(sorted_pokers):
        # 两对
        pokers_list = []
        # x x y y z
        if sorted_pokers[0].num == sorted_pokers[1].num and \
                sorted_pokers[2].num == sorted_pokers[3].num and \
                sorted_pokers[1].num != sorted_pokers[2].num and \
                sorted_pokers[3].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[2])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(3, pokers_list)
        # x x y z z
        elif sorted_pokers[0].num == sorted_pokers[1].num and \
                sorted_pokers[3].num == sorted_pokers[4].num and \
                sorted_pokers[1].num != sorted_pokers[2].num and \
                sorted_pokers[2].num != sorted_pokers[3].num:
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[2])
            return JudgeInfo(3, pokers_list)
        # x y y z z
        elif sorted_pokers[1].num == sorted_pokers[2].num and \
                sorted_pokers[3].num == sorted_pokers[4].num and \
                sorted_pokers[0].num != sorted_pokers[1].num and \
                sorted_pokers[2].num != sorted_pokers[3].num:
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[0])
            return JudgeInfo(3, pokers_list)
        else:
            return False

    @staticmethod
    def is_one_pair(sorted_pokers):
        # 一对
        pokers_list = []
        if sorted_pokers[0].num == sorted_pokers[1].num and \
                sorted_pokers[1].num != sorted_pokers[2].num and \
                sorted_pokers[2].num != sorted_pokers[3].num and \
                sorted_pokers[3].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[2])
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(2, pokers_list)
        elif sorted_pokers[0].num != sorted_pokers[1].num and \
                sorted_pokers[1].num == sorted_pokers[2].num and \
                sorted_pokers[2].num != sorted_pokers[3].num and \
                sorted_pokers[3].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(2, pokers_list)
        elif sorted_pokers[0].num != sorted_pokers[1].num and \
                sorted_pokers[1].num != sorted_pokers[2].num and \
                sorted_pokers[2].num == sorted_pokers[3].num and \
                sorted_pokers[3].num != sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[2])
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[4])
            return JudgeInfo(2, pokers_list)
        elif sorted_pokers[0].num != sorted_pokers[1].num and \
                sorted_pokers[1].num != sorted_pokers[2].num and \
                sorted_pokers[2].num != sorted_pokers[3].num and \
                sorted_pokers[3].num == sorted_pokers[4].num:
            pokers_list.append(sorted_pokers[3])
            pokers_list.append(sorted_pokers[0])
            pokers_list.append(sorted_pokers[1])
            pokers_list.append(sorted_pokers[2])
            return JudgeInfo(2, pokers_list)
        else:
            return False

    @staticmethod
    def get_pokers_info(pokers):
        if Poker.is_royal_straight_flush(pokers):
            j_type = "大同花顺"
            j_info = Poker.is_royal_straight_flush(pokers)
        elif Poker.is_straight_flush(pokers):
            j_type = "同花顺"
            j_info = Poker.is_straight_flush(pokers)
        elif Poker.is_four_of_a_kind(pokers):
            j_type = "四条"
            j_info = Poker.is_four_of_a_kind(pokers)
        elif Poker.is_full_house(pokers):
            j_type = "满堂红"
            j_info = Poker.is_full_house(pokers)
        elif Poker.is_flush(pokers):
            j_type = "同花"
            j_info = Poker.is_flush(pokers)
        elif Poker.is_straight(pokers):
            j_type = "顺子"
            j_info = Poker.is_straight(pokers)
        elif Poker.is_three_of_a_kind(pokers):
            j_type = "三条"
            j_info = Poker.is_three_of_a_kind(pokers)
        elif Poker.is_two_pair(pokers):
            j_type = "两对"
            j_info = Poker.is_two_pair(pokers)
        elif Poker.is_one_pair(pokers):
            j_type = "一对"
            j_info = Poker.is_one_pair(pokers)
        else:
            j_type = "散牌"
            j_info = JudgeInfo(1, pokers)
        return j_type, j_info
