A = matrix([[1,2],[3,4]])

print("The transformation caused by:")
show(A)
plot(vector([1,0]), color="#f88") + \
plot(vector([0,1]), color="#88f") + \
plot(A*vector([1,0]), color="#f00") + \
plot(A*vector([0,1]), color="#00f") + \
polygon([
    vector([0,0]),
    vector([1,0]),
    vector([1,1]),
    vector([0,1]),
    ], color="#fbf"
)+ \
polygon([
    A*vector([0,0]),
    A*vector([1,0]),
    A*vector([1,1]),
    A*vector([0,1]),
    ], color="#f0f"
)