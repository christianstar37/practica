def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    print(sum(hand)/len(hand), ':::', (hand[0]+hand[-1])/2, ':::', hand[len(hand)//2])
    strat_1 = sum(hand)/len(hand) == (hand[0]+hand[-1])/2
    strat_2 = sum(hand)/len(hand) == hand[len(hand)//2]
    return strat_1 or strat_2


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return sum(hand[0::2])/len(hand[0::2]) == sum(hand[1::2])/len(hand[1::2])


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    return (hand[:-1] + [hand[-1]*2]) if hand[-1] == 11 else hand

print(maybe_double_last([2,3,4,8,11]))
print(maybe_double_last([0,1,5]))