def fusion(t1,t2):
    # Si t1 est vide:
    if len(t1) == 0:
        # renvoyer t2
        return t2
    # Sinon si t2 est vide:
    elif len(t2) == 0:
        # renvoyer t1
        return t1
    else:
        # Si t1[0]<t2[0]:
        if t1[0]<t2[0]:
        #     retourner t1[0] + fusion(t1 sauf t1[0], t2)
            return [t1[0]] + fusion(t1[1:],t2)
        else:
        #     returner t2[0] + fusion(t1, t2 sauf t2[0])
            return [t2[0]] + fusion(t1, t2[1:])


def tri_fusion(T):
    if len(T) == 1:
        return T
    else:
        middle = len(T) // 2
        return fusion(tri_fusion(T[:middle]), tri_fusion(T[middle:]))

print(tri_fusion([ 2000, 1998, 2005, 2016, 2003, 2020, 1992]))