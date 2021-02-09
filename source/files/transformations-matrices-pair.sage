a = vector([1,-3,5])
b = vector([-4,2,3])
c = vector([3,0,4])

sum([plot(t/50*a+(50-t)/50*b,color='blue') for t in range(50+1)]) + \
    line([a,b],color='purple') + \
    sum([plot(t/50*b+(50-t)/50*c,color='red') for t in range(50+1)]) + \
    line([b,c],color='purple')
