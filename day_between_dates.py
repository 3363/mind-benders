# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def resetMonths(year):
    if isLeapYear(year):
        daysOfMonths[1] = 29
    else:
        daysOfMonths[1] = 28

def days_until_date(m, d, y): 
    # excluding last day
    resetMonths(y)
    
    m_idx = m - 1
    idx = 0
    day_until = 0
    while idx < m_idx:
        day_until += daysOfMonths[idx]
        idx += 1
    day_until += d - 1 
    return day_until

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    answer = 0

    # calculate full years
    i = y1 + 1 #start from the first full year
    while i < y2: # untill the last full year, exculding
        if isLeapYear(i):
            answer += 366
        else:
            answer += 365
        i += 1

    # days in first year
    if isLeapYear(y1):
        answer = answer + 366 - days_until_date(m1, d1, y1)
    else:
        answer = answer + 365 - days_until_date(m1, d1, y1)

    # days in last year
    answer = answer + days_until_date(m2, d2, y2)

    return answer

print daysBetweenDates(1930, 3, 3, 2012, 12, 12)
