from model.Poker import Poker


def main():
    print("#==================================#")
    print("    澳门葡京线上赌场，性感荷官在线发牌    ")
    print("#==================================#\n")

    # 洗牌
    poker_list = Poker.shuffle_pokers()

    # 发牌
    pokers_a = Poker.sort_pokers(Poker.deal_pokers(poker_list, 5))
    pokers_b = Poker.sort_pokers(Poker.deal_pokers(poker_list, 5))

    # 获取类型及相关信息
    type_a, j_info_a = Poker.get_pokers_info(pokers_a)
    type_b, j_info_b = Poker.get_pokers_info(pokers_b)

    # 输出手牌信息
    print("A:", type_a, pokers_a)
    print("B:", type_b, pokers_b)

    # 判断结果
    if j_info_a > j_info_b:
        print("\nA 获胜\n")
    elif j_info_a < j_info_b:
        print("\nB 获胜\n")
    else:
        print("\n平局\n")

    # 调试用：查看 判断信息
    # print("Judge_Info_A:", j_info_a)
    # print("Judge_Info_B:", j_info_b)


main()
