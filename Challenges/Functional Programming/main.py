from datetime import datetime
import operator

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000},
]


def classify_by_phone_number(records):
    classified_records = []

    permanent_charge = 0.36
    daytime_tax = 0.09
    nocturnal_tax = 0.0
    price_per_day = 86.4

    for record in records:
        start = convert_epoch_to_date(record['start'])
        end = convert_epoch_to_date(record['end'])

        total_price = permanent_charge + get_total_price(start,
        end, price_per_day, daytime_tax, nocturnal_tax)

        already_exists = False
        total_price = float('{0:.2f}'.format(total_price))

        for classified in classified_records:
            if classified['source'] == record['source']:
                already_exists = True

                classified['total'] = float('{0:.2f}'
                .format(classified['total'] + total_price))

        if not already_exists:
            classified_records.append({
                'source': record['source'],
                'total': total_price
            })

    classified_records = sort_records(classified_records)

    return classified_records


def sort_records(classified_records):
    return sorted(classified_records, key=lambda k: k['total'])[::-1]


def get_total_price(start, end, price_per_day, daytime_tax, nocturnal_tax):
    total = get_number_days(start, end) * price_per_day
    end_interval = end['time']['hour']

    if end['time']['hour'] < start['time']['hour']:
        end_interval += 24

    if end['time']['hour'] != start['time']['hour']:
        if 6 <= start['time']['hour'] < 22:
            total += (60 - (start['time']['minutes'] + 1)) * daytime_tax

        if 6 <= end['time']['hour'] < 22:
            total += (end['time']['minutes']) * daytime_tax

    else:
        if 6 <= start['time']['hour'] < 22:
            total += ((end['time']['minutes'])
            - (start['time']['minutes'] + 1)) * daytime_tax

    if end['time']['seconds'] >= start['time']['seconds'] \
    and 6 <= start['time']['hour'] < 22 and 6 <= end['time']['hour'] < 22:
        total += daytime_tax

    for hour in range(start['time']['hour'] + 1, end_interval):
        current_hour = 24 - hour if hour > 23 else hour
 
        if 6 <= current_hour < 22:
            total += (60 * daytime_tax)

    return total


def get_number_days(start, end):
    next_year = False
    days = 0

    if not end['day'] < start['day']:
        days += end['day'] - start['day']
    else:
        days += get_days_in_month(start['month'], start['year']) \
        - start['day'] + end['day']

    if end['month'] < start['month']:
        next_year = True

    if end['month'] - start['month'] > 1 \
    or (next_year and (12 - start['month']) + end['month'] > 1):
        days += get_months_difference_in_days(start['month'] + 1,
        end['month'], start['year'], end['year'])
    
    if end['year'] - start['year'] > 1:
        days += get_years_difference_in_days(start['year'] + 1, end['year'])

    return days


def get_days_in_month(month, year):
    months_thirty_one = [1, 3, 5, 7, 8, 10, 12]

    if month in months_thirty_one:
        return 31
    
    elif month == 2 and is_leap_year(year):
        return 29
    
    elif month == 2:
        return 28
    
    return 30


def get_years_difference_in_days(year_start, year_end):
    number_days = 0
    
    for year in range(year_start, year_end):
        if is_leap_year(year):
            number_days += 366
        else:
            number_days += 365

    return number_days


def is_leap_year(year):  
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_months_difference_in_days(month_start, month_end, year_start, year_end):
    number_days = 0
    end_interval = month_end

    if month_end < month_start:
        end_interval += 12

    for month in range(month_start, end_interval + 1):
        current_month = 12 - month if month > 12 else month

        number_days += get_days_in_month(current_month, year_start)

    return number_days


def convert_epoch_to_date(epoch):
    date = datetime.fromtimestamp(epoch).strftime('%m, %d, %X, %Y') \
    .replace(' ', '').split(',')

    return {
        'month': int(date[0]),
        'day': int(date[1]),
        'time': get_formatted_time(date[2]),
        'year': int(date[3])
    }


def get_formatted_time(time):
    formatted_time = time.split(':')
    return {
        'hour': int(formatted_time[0]),
        'minutes': int(formatted_time[1]),
        'seconds': int(formatted_time[2])
    }
