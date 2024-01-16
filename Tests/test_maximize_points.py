import Codewars.MaximizePoints as maximize_points

sample_test_cases = [
    ([3, 2, 4],  [1, 2, 3],  3),
    ([1],  [99],  0),
    ([99],  [1],  1),
    ([25, 7, 26, 48],  [1, 36, 5, 33],  3),
    ([7, 19, 23, 18, 38, 37, 38, 40],  [21, 12, 1, 0, 13, 38, 25, 49],  7),
]
@test.describe('Sample tests')
def sample_tests():
    @test.it('')
    def _():
        for team1, team2, expected in sample_test_cases:
            msg = f'maximize_points({team1}, {team2})'
            test.assert_equals(maximize_points(team1, team2), expected, msg)