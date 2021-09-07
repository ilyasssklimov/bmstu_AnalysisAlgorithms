from pprint import pprint


class AlgorithmError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        result = 'Incorrect name of algorithm, you should used ' \
                 '\'levenshtein_matrix\', \'damerau_levenshtein\', ' \
                 '\'levenshtein_recursively\', \'levenshtein_recursively_cache\''
        if self.message:
            result += f'. {self.message}'

        return result


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.algorithms_keys = {
            'levenshtein_matrix': levenshtein_matrix,
            'damerau_levenshtein': damerau_levenshtein,
            'levenshtein_recursively': levenshtein_recursively,
            'levenshtein_recursively_cache': levenshtein_recursively_cache
        }

    def execute(self, str_1, str_2):
        if self.name in self.algorithms_keys:
            return self.algorithms_keys[self.name](str_1, str_2)
        else:
            raise AlgorithmError


def levenshtein_matrix(str_1, str_2):
    len_1, len_2 = len(str_1), len(str_2)
    matrix = [[], [i for i in range(len_1 + 1)]]

    for i in range(1, len_2 + 1):
        matrix[0], matrix[1] = matrix[1], [i]

        for j in range(1, len_1 + 1):
            replace_letter = 1 if str_2[i - 1] != str_1[j - 1] else 0
            matrix[1].append(
                min(
                    matrix[1][j - 1] + 1,
                    matrix[0][j] + 1,
                    matrix[0][j - 1] + replace_letter
                )
            )

    return matrix[1][len_1]


def damerau_levenshtein(str_1, str_2):
    print('You used damerau-levenshtein')


def levenshtein_recursively(str_1, str_2):
    print('You used levenshtein recursively')


def levenshtein_recursively_cache(str_1, str_2):
    print('You used levenshtein recursively cache')
