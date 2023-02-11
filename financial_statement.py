import numpy as np

# Data (len = 12)
REVENUE = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
EXPENSES = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


def profit_for_each_month ():
    """Profit for each month"""
    profit_each = []
    for i in range(12):
        profit_each.append(REVENUE[i] - EXPENSES[i])
    result_1 = np.round(profit_each)
    print ('The profit for each month is:', result_1)
    return profit_each


def pat_of_each_month ():
    """Profit after tax (PAT) of each month (tax rate: 30%)"""
    pat_each = []
    for i in range(12):
        pat_each.append(REVENUE[i]*0.7 - EXPENSES[i])
    result_2 = np.round(pat_each)
    print ('The profit after tax of each month is:', result_2)
    return pat_each


def pat_divided_rev(listname):
    """Profit margin for each month (PAT divided by revenue)"""
    margin_each = []
    for i in range (12):
        margin_each.append(listname[i]/REVENUE[i])
    result_3 = np.round(margin_each, 2)
    print ('The profit margin for each month is:', result_3)


def good_month(listname_2):
    """Good month (PAT > mean of the year)"""
    good = []
    mean_pat = np.mean(listname_2)
    for line in listname_2:
        if line > mean_pat:
            good.append(line)
    good_round = np.round(good)
    print ('The good months are:', good_round)


def bad_month(listname_3):
    """Bad year (PAT > mean of the year)"""
    bad = []
    mean_pat = np.mean(listname_3)
    for line in listname_3:
        if line < mean_pat:
            bad.append(line)
    bad_round = np.round(bad)
    print ('The bad months are:', bad_round)


def best_month(listname_4):
    """The best month (PAT was max)"""
    best = []
    max_pat = max(listname_4)
    max_pat_round = np.round(max_pat)
    print ('The best month is:', max_pat_round)


def worst_month(listname_5):
    """The worst month (PAT was min)"""
    worst = []
    min_pat = min(listname_5)
    min_pat_round = np.round(min_pat)
    print ('The worst minth is:', min_pat_round)


def main():
    """main function"""
    profit_for_each_month()
    pat = pat_of_each_month() # 因為function中有return，所以設定變數承接回傳值
    pat_divided_rev(pat) # 因為應用到pat function中的return值，所以參數設為pat
    good_month(pat)
    bad_month(pat)
    best_month(pat)
    worst_month(pat)


main()
