def lfsr(seed, taps, length):
    """
    LFSR Generator
    :param seed: Initial state as a list of bits (e.g., [1,0,0,1])
    :param taps: Positions used for XOR feedback (e.g., [0,3])
    :param length: Number of output bits to generate
    :return: List of generated bits
    """
    state = seed.copy()
    output = []

    for _ in range(length):
        # XOR the tap positions
        feedback = 0
        for t in taps:
            feedback ^= state[t]

        # Shift right and insert feedback at the leftmost bit
        output_bit = state[-1]
        output.append(output_bit)
        state = [feedback] + state[:-1]

    return output


# Example usage
seed = [1, 0, 0, 1]       # Initial state
taps = [0, 3]             # Feedback taps
length = 20               # Generate 20 bits

sequence = lfsr(seed, taps, length)
print("Generated sequence:", sequence)
