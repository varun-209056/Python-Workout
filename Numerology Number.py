m  = int(input("Enter your birth month (in number): "))
d = int(input("Enter your birthday: "))

if m <= 12 and m >=1:
    if m !=2:
        if d <=31 and d >=1:
            n = d % 10
            m = d // 10
            d_n = n+m

            x = m % 10
            y = m // 10
            m_n = x+y
            sum1 = d_n+m_n
            while sum1>9:
                s_a = sum1 % 10
                s_b = sum1 // 10
                sum1 = s_a + s_b
            print(f"Your numerology number is:{sum1} ")
        else:
            print("invalid input")
    elif m == 2:
        if d <=28 and d >=1:
            n = d % 10
            m = d // 10
            d_n = n+m

            x = m % 10
            y = m // 10
            m_n = x+y
            sum1 = d_n+m_n
            while sum1>9:
                s_a = sum1 % 10
                s_b = sum1 // 10
                sum1 = s_a + s_b
            print(f"Your numerology number is:{sum1}") 
        else:
            print("invalid input")
else:
    print("invalid input")
