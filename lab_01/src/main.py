from algorithm import Algorithm


def main():
    result = Algorithm('levenshtein_matrix')
    print(result.execute('abc', 'as'))


if __name__ == '__main__':
    main()
