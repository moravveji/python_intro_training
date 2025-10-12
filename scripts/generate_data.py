jdef main():
    print('case', 'dim', 'temp')
    case_nr = 0
    for dim_nr in [1, 2, 3]:
        for temp in [-0.5, 0.0, 0.5]:
            case_nr += 1
            print(case_nr, dim_nr, temp)
    return 0
