def perfometer_check_mk_apcupsd_outvoltage(row, check_command, perf_data):
    outvolt = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    mmax  = float(perf_data[0][6])

    perc = 100 * ( outvolt/mmax)

    if outvolt < crit:
        color = "#FF0000"
    elif outvolt < warn:
        color = "#FFFF00"
    else:
        color = "#357EC7"

    return "%.0fV" % outvolt, perfometer_linear(perc, color)



perfometers["check_mk-apcupsd.outvoltage"] = perfometer_check_mk_apcupsd_outvoltage
