def perfometer_check_mk_apcupsd_timeleft(row, check_command, perf_data):
    tleft = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    mmax  = float(perf_data[0][6])

    perc = 100 * ( tleft/mmax)

    if tleft < crit:
        color = "#FF0000"
    elif tleft < warn:
        color = "#FFFF00"
    else:
        color = "#00FF00"

    return "%.0f min" % tleft, perfometer_linear(perc, color)



perfometers["check_mk-apcupsd.timeleft"] = perfometer_check_mk_apcupsd_timeleft
