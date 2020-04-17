"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """

    # Return 0 if the the list is empty
    if hand == []:
        return 0

    score_set = set([])
    for item in hand:
        item_score = item * hand.count(item)
        score_set.add(item_score)

    return max(score_set)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # Generate all possible sequences of hand
    die_sides = list(range(1, num_die_sides+1))
    hand_sequences = gen_all_sequences(die_sides, num_free_dice)
    # Compute all possible scores
    scores = []
    for sequence in hand_sequences:
        hand = sequence + held_dice
        scores.append(score(hand))
    # Compute the expected value with this held_dice
    expected_value_var = float(sum(scores)) / len(scores)
    return expected_value_var


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set([()])
    for item in hand:
        temp_holds = set([])
        for subset in holds:
            new_subset = list(subset)
            new_subset.append(item)
            temp_holds.add(tuple(new_subset))
        holds.update(temp_holds)

    return holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    result = (0.0, ())
    current_value = float('-inf')

    # Generating all possible holds
    for hold in gen_all_holds(hand):
        value = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if value > current_value:
            current_value = value
            result = (current_value, hold)

    return result


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


# run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
