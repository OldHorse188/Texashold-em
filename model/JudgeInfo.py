# 判断信息类

class JudgeInfo:
    __slots__ = ("__typ", "__data")

    def __init__(self, typ, data):
        self.__typ = typ
        self.__data = data

    def __repr__(self):
        return "type=" + str(self.__typ) + ", data=" + str(self.__data)

    def __lt__(self, other):
        # 定义 < 运算
        if self.__typ < other.typ:
            return True
        elif self.__typ == other.typ:
            for d in range(0, len(self.__data)):
                if self.__data[d] < other.data[d]:
                    return True
                elif self.__data[d] > other.data[d]:
                    return False
            return False
        else:
            return False

    def __eq__(self, other):
        # 定义 == 运算
        if self.__typ == other.typ:
            for d in range(0, len(self.__data)):
                if self.__data[d] != other.data[d]:
                    return False
            return True
        else:
            return False

    @property
    def typ(self):
        return self.__typ

    @typ.setter
    def typ(self, typ):
        self.__typ = typ

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
