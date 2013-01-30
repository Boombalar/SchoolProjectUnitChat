import math
while True:
    et = input("Hvad kender du? (radius, korde, vinkel, pilhoejde) ")
    if et == "radius":
        r = input("Hvad er radius? ")
        r = float(r)
    if et == "korde":
        k = input("Hvad er korden? ")
        k = float(k)
    if et == "vinkel":
        V = input("Hvad er vinklen? ")
        V = float(V)
    if et == "pilhoejde":
        ph = input("Hvad er pilhøjden? ")
        ph = float(ph)
    to = input("Hvad kender du? (radius, korde, vinkel, pilhoejde) ")
    if to == "radius":
        r = input("Hvad er radius? ")
        r = float(r)
    if to == "korde":
        k = input("Hvad er korden? ")
        k = float(k)
    if to == "vinkel":
        V = input("Hvad er vinklen? ")
        V = float(V)
    if to == "pilhoejde":
        ph = input("Hvad er pilhøjden? ")
        ph = float(ph)
        
    if et == "vinkel":
        v = (math.pi*V)/180
    if to == "vinkel":
        v = (math.pi*V)/180
        
    if et == "korde":
        if to == "radius":
            v = 2 * math.asin(k/(2*r))
            ph = r * (1 - math.cos(v/2))
    if et == "radius":
        if to == "korde":
            v = 2 * math.asin(k/(2*r))
            ph = r * (1 - math.cos(v/2))
            
    if et == "radius":
        if to == "vinkel":
            k = 2 * r * math.sin(v/2)
            ph = r * (1 - math.cos(v/2))
    if et == "vinkel":
        if to == "radius":
            k = 2 * r * math.sin(v/2)
            ph = r * (1 - math.cos(v/2))

    if et == "radius":
        if to == "pilhoejde":
            v = 2*math.acos((r-ph)/r)
    if et == "pilhoejde":
        if to == "radius":
            v = 2*math.acos((r-ph)/r)

    if et == "korde":
        if to == "vinkel":
            r = 0.5 * k/math.sin(0.5*v)
            ph = r * (1 - math.cos(v/2))
    if et == "vinkel":
        if to == "korde":
            r = 0.5 * k/math.sin(0.5*v)
            ph = r * (1 - math.cos(v/2))

    if et == "korde":
        if to == "pilhoejde":
            r = ph/2 + (k*k)/(8*ph)
    if et == "pilhoejde":
        if to == "korde":
            r = ph/2 + (k*k)/(8*ph)

    if et == "vinkel":
        if to == "pilhoejde":
            r = -(ph/(-1+math.cos(0.5*v)))
    if to == "vinkel":
        if et == "pilhoejde":
            r = -(ph/(-1+math.cos(0.5*v)))
            
    d = r * 2
    o = r * 2 * math.pi
    a = r * r * math.pi
    v = 2*math.acos((r-ph)/r)
    ph = r * (1 - math.cos(v/2))
    k = 2 * r * math.sin(v/2)
    V = 180*v/math.pi

    print("Radius:", r)
    print("Diameter:",d)
    print("Omkreds:",o)
    print("Areal:",a)
    print("Vinkel:",V)
    print("Korden:",k)
    print("Pilhoejde:",ph)

