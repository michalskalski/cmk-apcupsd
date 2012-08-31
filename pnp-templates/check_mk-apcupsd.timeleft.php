<?php
$opt[1] = "--vertical-label \"Minutes\"  -l 0 -u 60 --title \"$servicedesc\" ";


$def[1] = "DEF:var1=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:var1#80f000:\"Time left\:\" ";
$def[1] .= "GPRINT:var1:LAST:\"%2.0lf min\" ";
$def[1] .= "LINE1:var1#800040:\"\" ";
$def[1] .= "GPRINT:var1:MAX:\"(Max\: %2.0lf min,\" ";
$def[1] .= "GPRINT:var1:AVERAGE:\"Avg\: %2.0lf min)\" ";
$def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1] min\" ";


?>
