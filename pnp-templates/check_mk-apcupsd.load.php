<?php
$opt[1] = "--vertical-label \"Percent\" -l 0 -u 100 --title \"$servicedesc\" ";
$def[1] = "DEF:var2=$RRDFILE[1]:$DS[1]:MIN ";
$def[1] .= "AREA:var2#80e0c0:\"Capacity\:\" ";
$def[1] .= "GPRINT:var2:LAST:\"%2.0lf%%\" ";
$def[1] .= "LINE1:var2#008040:\"\" ";
$def[1] .= "GPRINT:var2:MAX:\"(Max\: %2.0lf%%,\" ";
$def[1] .= "GPRINT:var2:AVERAGE:\"Avg\: %2.0lf%%)\" ";
$def[1] .= "HRULE:$WARN[1]#FFFF00:\"Warning\: $WARN[1]%\" ";
$def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1]%\" ";

?>
