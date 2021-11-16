"""
aki: 411381200109225325
"""
def last_dit_calculator(digs):
    """
    >>> last_dit_calculator('12345678912345678')
    '3'
    """
    assert len(digs) == 17 and digs.isdigit(), 'incorrect input'
    return (['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][
        sum([int(digs[i]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][i] for i in range(17)]) % 11])


last = '5'
str_year = "2001"
str_region = "411381"
before_last = "532"
for month in range(1, 13):
    for day in range(1, 32):
        if month < 10:
            str_month = '0' + str(month)
        else:
            str_month = str(month)
        if day < 10:
            str_day = '0' + str(day)
        else:
            str_day = str(day)
        digs = str_region + str_year + str_month + str_day + before_last
        if last_dit_calculator(digs) == last:
            print(digs + last)