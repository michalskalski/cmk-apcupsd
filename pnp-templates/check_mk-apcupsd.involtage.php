<?php
$opt[1] = "--vertical-label \"Volt\" --title \"$servicedesc\" ";
$def[1] = "DEF:volt=$RRDFILE[1]:$DS[1]:MIN ";
$def[1] .= "GPRINT:volt:LAST:\"%2.0lfV\" ";
$def[1] .= "LINE1:volt#3300FF:\"\" ";
$def[1] .= "GPRINT:volt:MIN:\"(min\: %2.0lfV,\" ";
$def[1] .= "GPRINT:volt:MAX:\"max\: %2.0lfV,\" ";
$def[1] .= "GPRINT:volt:AVERAGE:\"avg\: %2.0lfV)\" ";
$def[1] .= "HRULE:$WARN[1]#FFFF00:\"Warning\: $WARN[1]V\" ";
$def[1] .= "HRULE:$CRIT[1]#FF0000:\"Critical\: $CRIT[1]V\" ";

?>
