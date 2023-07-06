#商业贷款 五年及以下4.75% 五年以上4.90%
#公积金贷款 五年及以下2.75% 五年以上3.25%
#组合贷款
"""
每月月供参考 = 贷款金额 × [月利率 × (1 + 月利率)  ^ 还款月数] ÷ { [(1 +月利率)  ^ 还款月数] - 1}
还款总额 = 每月月供参考 × 期限 × 12
支付利息 = 还款总额 - 贷款金额 × 10000
"""
choice = int(input("是否为组合贷款：1.yes2.no"))


if choice == 2:
    a = float(input("输入贷款金额（万）"))
    d = float(input("输入期限（年）"))
    choice2 = int(input("贷款类型：1.商业贷款2.公积金贷款"))
    if choice2 == 1:
        while d > 5:
            l = 0.049
            uu = a * (l/12 * (1 + l/12)**(d*12)) / (((1 + l / 12) ** (d*12)) - 1)
            ii = uu * d * 12
            oo = ii - a

            print("月供参考=", uu)
            print("还款总额=", ii)
            print("支付利息=", oo)
            break
        while d <= 5:
            l = 0.0475
            uu = a * (l / 12 * (1 + l / 12) ** (d * 12)) / (((1 + l / 12) ** (d * 12)) - 1)
            ii = uu * d * 12
            oo = ii - a
            print("月供参考=", uu)
            print("还款总额=", ii)
            print("支付利息=", oo)
            break

    if choice2 == 2:
        while d > 5:
            k = 0.0325
            uu = a * (k / 12 * (1 + k / 12) ** (d * 12)) / (((1 + k / 12) ** (d * 12)) - 1)
            ii = uu * d * 12
            oo = ii - a
            print("月供参考=", uu)
            print("还款总额=", ii)
            print("支付利息=", oo)
            break
        while d <= 5:
            k = 0.0275
            uu = a * (k / 12 * (1 + k / 12) ** (d * 12)) / (((1 + k / 12) ** (d * 12)) - 1)
            ii = uu * d * 12
            oo = ii - a
            print("月供参考=", uu)
            print("还款总额=", ii)
            print("支付利息=", oo)
            break
if choice == 1:
    nn = float(input("输入商业贷款金额："))
    n = float(input("输入商业贷款年限"))
    while n > 5:
        p = 0.0490
        u = nn * (p / 12 * (1 + p / 12) ** (n * 12)) / (((1 + p / 12) ** (n * 12)) - 1)
        i = u * n * 12
        o = i - nn
        print("商业贷款月供参考=", u)
        print("商业贷款还款总额=", i)
        print("商业贷款支付利息=", o)
        break
    while n <= 5:
        p = 0.0750
        u = nn * (p / 12 * (1 + p / 12) ** (n * 12)) / (((1 + p / 12) ** (n * 12)) - 1)
        i = u * n * 12
        o = i - nn
        print("商业贷款月供参考=", u)
        print("商业贷款还款总额=", i)
        print("商业贷款支付利息=", o)
        break

    mm = float(input("输入公积金贷款金额："))
    m = float(input("输入公积金贷款年限"))
    while m > 5:
        r = 0.0325
        uuu = mm * (r / 12 * (1 + r / 12) ** (m * 12)) / (((1 + r / 12) ** (m * 12)) - 1)
        iii = uuu * m * 12
        ooo = iii - mm
        print("公积金贷款月供参考=", uuu)
        print("公积金贷款还款总额=", iii)
        print("公积金贷款支付利息=", ooo)
        break
    while m <= 5:
        r = 0.0275
        uuu = mm * (r / 12 * (1 + r / 12) ** (m * 12)) / (((1 + r / 12) ** (m * 12)) - 1)
        iii = uuu * m * 12
        ooo = iii - mm
        print("公积金贷款月供参考=", uuu)
        print("公积金贷款还款总额=", iii)
        print("公积金贷款支付利息=", ooo)
        break

