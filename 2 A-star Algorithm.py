dict_hn = {
    'A':10,'B':20,'C':30,'D':40,'E':50,'F':60,'G':70,'H':80,'I':90,
    'L':100,'M':110,'N':120,'O':130,'P':140,'R':150,'S':160,
    'T':170,'U':180,'V':190,'Z':200
}

dict_gn = dict(
    A=dict(Z=5, T=50, S=100),
    B=dict(U=50, G=90, P=100, F=200),
    C=dict(D=120, P=140, R=150),
    D=dict(M=75, C=100),
    E=dict(H=80),
    F=dict(S=90, B=200),
    G=dict(B=80),
    H=dict(E=80, U=90),
    I=dict(N=85, V=95),
    L=dict(M=70, T=110),
    M=dict(L=70, D=75),
    N=dict(I=85),
    O=dict(Z=70, S=150),
    P=dict(R=95, B=105, C=135),
    R=dict(S=80, P=90, C=140),
    S=dict(R=80, F=90, A=140, O=150),
    T=dict(L=110, A=120),
    U=dict(B=80, H=90, V=140),   # fixed Bu → B
    V=dict(I=90, U=140),
    Z=dict(O=70, A=75)
)

import queue as Q

start = 'A'
goal = 'B'
result = ''


def get_fn(citystr):
    cities = citystr.split(" , ")
    hn = 0
    gn = 0

    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]

    hn = dict_hn[cities[len(cities) - 1]]

    return (hn + gn)


def expand(cityq):
    global result

    tot, citystr, thiscity = cityq.get()

    if thiscity == goal:
        result = citystr + " : : " + str(tot)
        return

    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr + " , " + cty), citystr + " , " + cty, cty))

    expand(cityq)


def main():
    cityq = Q.PriorityQueue()
    thiscity = start

    cityq.put((get_fn(start), start, thiscity))

    expand(cityq)

    print("The A* path with the total is:")
    print(result)


main()
