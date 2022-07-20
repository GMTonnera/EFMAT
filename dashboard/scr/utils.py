import math


def format_date(year, month, day):
    if month > 9:
        str_month = str(month)
    else:
        str_month = "0" + str(month)

    if day > 9:
        str_day = str(day)
    else:
        str_day = "0" + str(day)

    return f"{year}-{str_month}-{str_day}"


def make_select_list(lis):
    l = []
    for item in lis:
        l.append({"label": item, "value": item})
    
    return l
    

def calculte_date(start_date, period):
    date = ""
    year = int(start_date[:4])
    month = int(start_date[5:7]) + period
    day = start_date[8:]
    
    if month > 12:
        month -= 12
        year += 1

    year = str(year)
    
    if month > 9:
        month = str(month)
    else:
        month = "0" + str(month)

    date = "-".join([year, month, day])        
    
    return date


def find_date(wallet, date):
    s_date = [int(num) for num in date.split("-")]
    while True:
        new_date = format_date(s_date[0],s_date[1],s_date[2])
        if wallet.check_date(new_date):
            return new_date
        
        else:
            s_date[2] += 1
            if s_date[2] > 31:
                s_date[2] -= 30
                s_date[1] += 1
                if s_date[1] > 12:
                    s_date[1] -= 12
                    s_date[0] += 1

