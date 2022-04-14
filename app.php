<?php

function fusion($t1,$t2) {
    if(count($t1) === 0) {
        return $t2;
    }
    else if(count($t2) === 0) {
        return $t1;
    }
    else {
        if($t1[0]<$t2[0]) {
            // tableau.slice(1) -> A partir de l'élément jusqu'à la fin
            return array_merge([$t1[0]],fusion(array_slice($t1,1),$t2));
        }
        else {
            return array_merge([$t2[0]],fusion($t1, array_slice($t2,1)));
        }
    }

}

function tri_fusion($T) {
    if(count($T) === 1) {
        return $T;
    }
    else {
        $middle = floor(count($T) / 2);
        return fusion(tri_fusion(array_slice($T,0, $middle)), tri_fusion(array_slice($T,$middle)));
    }

}


print_r(tri_fusion([ 2000, 1998, 2005, 2016, 2003, 2020, 1992]));