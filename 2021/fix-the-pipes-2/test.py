from solution import check_pipe as cp


def main():
    for i, case in enumerate(test_cases):
        print(i)
        result = cp.check_pipe(case[0])
        print("case:", case)
        print("expected:", case[1])
        print("actual:", result)
        if case[1] == result:
            print("*** Success ***")
        else:
            print("--- FAILURE ---")
        print()


test_cases = [
    (['╋━━┓',
      '┃..┃',
      '┛..┣'],
     True),

    (['...┏',
      '┃..┃',
      '┛..┣'],
     False),

    (['...┏',
      '...┃',
      '┛..┣'],
     False),

    (['...┏',
      '...┃',
      '┓..┣'],
     True),

    (['╋',
      '╋',
      '╋'],
     True),

    (['╋....',
      '┃..┛.',
      '┃....'],
     False),

    (['....',
      '.┛┛.',
      '....'],
     True),
]


# @test.describe('Sample tests')
# def sample_tests():
#     @test.it('Check the leaking')
#     def tests():
#         for pipe, expected in test_cases:
#             pipe_str = '\n'.join(pipe)
#             actual = check_pipe(pipe)
#             test.expect(actual == expected, f'{actual} should equal {expected}\n{pipe_str}')


if __name__ == "__main__":
    main()
