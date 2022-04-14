function fusion(t1,t2) {
    if(t1.length === 0) {
        return t2;
    }
    else if(t2.length === 0) {
        return t1;
    }
    else {
        if(t1[0]<t2[0]) {
            // tableau.slice(1) -> A partir de l'élément jusqu'à la fin
            return [].concat([t1[0]],fusion(t1.slice(1),t2));
        }
        else {
            return [].concat([t2[0]],fusion(t1, t2.slice(1)));
        }
    }

}

function tri_fusion(T) {
    if(T.length === 1) {
        return T;
    }
    else {
        let middle = Math.floor(T.length / 2);
        return fusion(tri_fusion(T.slice(0, middle)), tri_fusion(T.slice(middle)));
    }

}


console.log(tri_fusion([ 2000, 1998, 2005, 2016, 2003, 2020, 1992]))