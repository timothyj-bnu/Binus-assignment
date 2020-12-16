
NUMBER_OF_BOX = 3
BALL_NUMBER_PERBOX = 2
RED_IN_BOX1 = 2
RED_IN_BOX2 = 1
RED_IN_BOX3 = 0
BALL_TAKEN = 1



def main():
    p_b = BALL_TAKEN / NUMBER_OF_BOX
    p_r_b1 = RED_IN_BOX1 / BALL_NUMBER_PERBOX
    p_r_b2 = RED_IN_BOX2 / BALL_NUMBER_PERBOX
    p_r_b3 = RED_IN_BOX3 / BALL_NUMBER_PERBOX

    p_b1_r = (p_r_b1 * p_b) / (p_r_b1 * p_b + p_r_b2 * p_b + p_r_b3 * p_b)
    p_b2_r = (p_r_b2 * p_b) / (p_r_b1 * p_b + p_r_b2 * p_b + p_r_b3 * p_b)
    p_b3_r = (p_r_b3 * p_b) / (p_r_b1 * p_b + p_r_b2 * p_b + p_r_b3 * p_b)
    print("Probability of taking one ball from each box P(B1,2,3) : %0.2f" % (p_b))
    print("Probability of taking one red ball from each boxes : ")
    print("P(R|B1) : %0.2f" % p_r_b1)
    print("P(R|B2) :%0.2f" % p_r_b2)
    print("P(R|B3) :%0.2f" % p_r_b3)
    print("Probability of getting red ball from each boxes: ")
    print("Box 1 : %0.2f" % p_b1_r)
    print("Box 2 : %0.2f" % p_b2_r)
    print("Box 3 : %0.2f" % p_b3_r)


if __name__ == '__main__':
    main()