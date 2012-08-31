<?php
$opt[1] = "--vertical-label \"Celsius\"  -l $MIN[1]  -u $MAX[1] --title \"$servicedesc\" ";

$color = sprintf("ff%02x80", $ACT[1] * 3, $ACT[1] * 2);

$def[1] = "DEF:var1=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:var1#$color:\"Temperature\:\" ";
$def[1] .= "GPRINT:var1:LAST:\"%2.0lfC\" ";
$def[1] .= "LINE1:var1#800040:\"\" ";
$def[1] .= "GPRINT:var1:MAX:\"(Max\: %2.0lfC,\" ";
$def[1] .= "GPRINT:var1:AVERAGE:\"Avg\: %2.0lfC)\" ";
$def[1] .= "HRULE:$WARN[1]#FFFF00:\"Warning\: $WARN[1]C\" ";
$def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1]C\" ";


?>
