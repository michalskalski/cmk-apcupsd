def perfometer_check_mk_apcupsd_bvoltage(row, check_command, perf_data):
    bvolt = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    mmax  = float(perf_data[0][6])

    perc = 100 * ( bvolt/mmax)

    if bvolt < crit:
        color = "#FF0000"
    elif bvolt < warn:
        color = "#FFFF00"
    else:
        color = "#357EC7"

    return "%.0fV" % bvolt, perfometer_linear(perc, color)



perfometers["check_mk-apcupsd.bvoltage"] = perfometer_check_mk_apcupsd_bvoltage
