import math

def frequency_test(sequence):
    """
    Frequency (Monobit) Test:
    Checks if the number of 1s and 0s are approximately equal.
    """
    n = len(sequence)
    s = sum(1 if bit == 1 else -1 for bit in sequence)
    test_stat = abs(s) / math.sqrt(n)
    return test_stat < 1.96  # 95% confidence interval


def runs_test(sequence):
    """
    Runs Test:
    Checks if the number of runs (consecutive identical bits) is as expected.
    """
    n = len(sequence)
    pi = sum(sequence) / n  # proportion of 1s
    if abs(pi - 0.5) > (2 / math.sqrt(n)):
        return False  # fails precondition

    runs = 1
    for i in range(1, n):
        if sequence[i] != sequence[i-1]:
            runs += 1

    expected_runs = 2 * n * pi * (1 - pi)
    z = abs(runs - expected_runs) / (2 * math.sqrt(2 * n) * pi * (1 - pi))
    return z < 1.96  # 95% confidence interval


# Example usage
sequence = [1,0,1,1,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1]

print("Frequency Test Passed:", frequency_test(sequence))
print("Runs Test Passed:", runs_test(sequence))
