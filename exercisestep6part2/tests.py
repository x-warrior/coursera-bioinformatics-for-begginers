import pytest

from exercisestep6part2.helpers import count_dict


@pytest.mark.parametrize('n, input, output', ((3, 'CGATATATCCATAG', {0: 1, 1: 1, 2: 3, 3: 2, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 3, 11: 1}),
                                              (5, 'CCGAACACCCGTACACCGAACACCACACCACACCTTGCACACCACACCTACACCACACACCACACCGGACACCCACACCCACACCACGAACACCGAGAGTACACCTA',     {0: 2, 1: 3, 2: 3, 3: 3, 4: 15, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2, 11: 3, 12: 15, 13: 3, 14: 2, 15: 2, 16: 3, 17: 3, 18: 3, 19: 15, 20: 6, 21: 6, 22: 7, 23: 9, 24: 15, 25: 6, 26: 6, 27: 7, 28: 9, 29: 15, 30: 3, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 9, 38: 15, 39: 6, 40: 6, 41: 7, 42: 9, 43: 15, 44: 3, 45: 2, 46: 1, 47: 1, 48: 3, 49: 15, 50: 6, 51: 6, 52: 7, 53: 9, 54: 1, 55: 9, 56: 15, 57: 6, 58: 6, 59: 7, 60: 9, 61: 15, 62: 3, 63: 1, 64: 1, 65: 1, 66: 1, 67: 1, 68: 15, 69: 3, 70: 2, 71: 2, 72: 7, 73: 9, 74: 15, 75: 3, 76: 2, 77: 2, 78: 7, 79: 9, 80: 15, 81: 6, 82: 6, 83: 1, 84: 1, 85: 1, 86: 3, 87: 3, 88: 3, 89: 15, 90: 3, 91: 2, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 2, 99: 3, 100: 15, 101: 3, 102: 2})))
def test_count_dict(n, input, output):
    assert count_dict(input, n) == output
