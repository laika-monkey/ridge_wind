def dtg2epoch(dtg):
    import calendar
    import datetime
    fmt = '%Y%m%d%H%M'
    dt = datetime.datetime.strptime(dtg, fmt)
    return calendar.timegm((dt.year, dt.month, dt.day, dt.hour, dt.minute, 0))

def convCoord(c):
    direction = c[-1:]
    value = float(c[:-1])
    negDir = ['W', 'S']
    value = value * -1 if direction in negDir else value
    return value
