def perfometer_check_mk_apcupsd_involtage(row, check_command, perf_data):
    involt = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    mmax  = float(perf_data[0][6])

    perc = 100 * ( involt/mmax)

    if involt < crit:
        color = "#FF0000"
    elif involt < warn:
        color = "#FFFF00"
    else:
        color = "#357EC7"

    return "%.0fV" % involt, perfometer_linear(perc, color)



perfometers["check_mk-apcupsd.involtage"] = perfometer_check_mk_apcupsd_involtage
