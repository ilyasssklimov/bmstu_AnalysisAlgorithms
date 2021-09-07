from lab_01.src.algorithm import Algorithm


def main():
    lev_mat = Algorithm('levenshtein_matrix')
    lev_rec = Algorithm('levenshtein_recursively')
    lev_rec_cache = Algorithm('levenshtein_recursively_cache')
    dam_lev = Algorithm('damerau_levenshtein')

    str_1, str_2 = 'универсaaaaasdasda', 'униfasdasdasеврси'
    print(str_1, str_2)

    print(lev_mat.execute(str_1, str_2), lev_mat.get_time(str_1, str_2))
    print(lev_rec.execute(str_1, str_2), lev_rec.get_time(str_1, str_2))
    print(lev_rec_cache.execute(str_1, str_2), lev_rec_cache.get_time(str_1, str_2))
    print(dam_lev.execute(str_1, str_2), dam_lev.get_time(str_1, str_2))


if __name__ == '__main__':
    main()
