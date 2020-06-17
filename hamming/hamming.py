def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Las cadenas de ADN son de distintas longitudes")

    elif len(strand_a) == len(strand_b):
        num = 0
        dis = 0
        for dato in strand_a:
            if dato != strand_b[num]:
                dis += 1
                num += 1
            else:
                num += 1
        return dis
    
    