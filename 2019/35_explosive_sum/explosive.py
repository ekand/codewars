def exp_sum(n):
    p = n


# calculation taken from here
    # https://math.stackexchange.com/questions/2675382/calculating-integer-partitions


    def pentagonal_number(k):
        return int(k * (3 * k - 1) / 2)

    def compute_partitions(goal):
        partitions = [1]
        for n in range(1, goal + 1):
            partitions.append(0)
            for k in range(1, n + 1):
                coeff = (-1) ** (k + 1)
                for t in [pentagonal_number(k), pentagonal_number(-k)]:
                    if (n - t) >= 0:
                        partitions[n] = partitions[n] + coeff * partitions[n - t]
        return partitions

    return (compute_partitions(n))[-1]