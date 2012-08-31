def perfometer_check_mk_apcupsd_load(row, check_command, perf_data):
    load = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])


    if load > warn:
        color = "#ffff00"
    elif load > crit:
        color = "#ff0000"
    else:
        color = "#00ff00"
    
    return "%.0f%%" % load, perfometer_linear(load, color)






perfometers["check_mk-apcupsd.load"] = perfometer_check_mk_apcupsd_load
