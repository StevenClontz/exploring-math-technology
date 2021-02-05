a = vector([5,-12])
b = vector([-3,4])

plot(a,color='blue') + \
    arrow(a,a+b,color='red') + \
    plot(a+b,color='purple')
