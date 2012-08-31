def perfometer_check_mk_apcupsd_temp(row, check_command, perf_data):
    temp = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    mmax = float(perf_data[0][6])

    perc = 100 * (temp / mmax)

    if temp > warn:
        color = "#ffff00"
    elif temp > crit:
        color = "#ff0000"
    else:
        color = "#00ff00"

    return "%.0fC" % temp, perfometer_linear(perc, color)






perfometers["check_mk-apcupsd.temp"] = perfometer_check_mk_apcupsd_temp 
