from lab_01.src.algorithm import Algorithm


def main():
    result = Algorithm('levenshtein_recursively')
    print(result.execute('скат', 'кот'))


if __name__ == '__main__':
    main()
