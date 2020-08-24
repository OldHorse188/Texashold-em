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
