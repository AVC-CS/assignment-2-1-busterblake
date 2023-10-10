def main():
    num_male = int(input('Number of males: ' ))
    num_female = int(input('Number of females: ' ))


    total = num_male + num_female


    m_perc = (100 * num_male)/total
    f_perc = (100 * num_female)/total



    print(f"{round(m_perc,2)} % are male")
    print(f"{round(f_perc,2)} % are female")

    return m_perc, f_perc


if __name__ == '__main__':
    main()
