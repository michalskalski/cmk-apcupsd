def perfometer_check_mk_apcupsd_bcharge(row, check_command, perf_data):
    bcharge = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])


    if bcharge < crit:
        color = "#FF0000"
    elif bcharge < warn:
        color = "#FFFF00"
    else:
        color = "#00FF00"

    return "%.0f%%" % bcharge, perfometer_linear(bcharge, color)



perfometers["check_mk-apcupsd.bcharge"] = perfometer_check_mk_apcupsd_bcharge
