from hexlet_challenges import __version__, lists


def test_version():
    assert __version__ == '0.1.0'


def test_is_continuous_sequence():
    assert not lists.is_continuous_sequence([])
    assert not lists.is_continuous_sequence([7])
    assert not lists.is_continuous_sequence([5, 3, 2, 8])
    assert not lists.is_continuous_sequence([10, 11, 12, 14, 15])
    assert not lists.is_continuous_sequence([10, 11, 11, 12])
    assert lists.is_continuous_sequence([0, 1, 2, 3])
    assert lists.is_continuous_sequence([-5, -4, -3])
    assert lists.is_continuous_sequence([10, 11, 12, 13])
