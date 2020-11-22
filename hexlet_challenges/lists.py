def is_continuous_sequence(sequense):
    """Реализуйте функцию is_continuous_sequence.

    которая проверяет, является ли переданная последовательность
    целых чисел возрастающей непрерывно (не имеющей пропусков чисел).
    Например, последовательность [4, 5, 6, 7] — непрерывная,
    а [0, 1, 3] — нет.
    Последовательность может начинаться с любого числа.
    Главное условие — отсутствие пропусков чисел.
    Последовательность из одного числа не может считаться возрастающей.

    Args:
        sequense ([type]): [description]

    Returns:
        [type]: [description]
    """
    if len(sequense) <= 1:
        return False
    for index, item in enumerate(sequense[:-1]):
        if item + 1 != sequense[index + 1]:
            return False
    return True
