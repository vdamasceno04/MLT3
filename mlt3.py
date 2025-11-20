def mlt3_encode(bin):
    v = 5
    mlt3 = []
    last_non_zero = -v
    state = 0
    for bit in bin:
        if bit == '0':
            mlt3.append(state)
        elif bit == '1':
            if state == v or state == -v:
                state = 0
                mlt3.append(state)
            else:
                last_non_zero *= -1
                state = last_non_zero
                mlt3.append(state)
            
    return mlt3


def mlt3_decode(mlt3):
    bin = []
    state = 0
    for value in mlt3:
        if value == state:
            bin.append(0)
        else:
            bin.append(1)
        state = value

    return ''.join(str(num) for num in bin)