basic1 = veci # first basic vector
basic2 = vecj # second basic vector

# draws part of coordinate system based on chosen basis
size = 6
sum(
    [line([n*basic1-size*basic2,n*basic1+size*basic2],color="#ddf") for n in range(-size,size+1)] + \
    [line([n*basic2-size*basic1,n*basic2+size*basic1],color="#ddf") for n in range(-size,size+1)] + \
    [line([-size*basic2,size*basic2],color="#88f"),line([-size*basic1,size*basic1],color="#88f")]
) + plot(basic1,color="#f88") + plot(basic2,color="#f88") + \
    plot(vector([-1,3]))
