A = matrix([
    [3,0,-2],
    [1,-1,3],
    [0,-1,1],
])
print("The determinant of")
show(A)
print("is")
show(det(A))
corners = [
    vector([0,0,0]),
    vector([0,0,1]),
    vector([0,1,0]),
    vector([0,1,1]),
    vector([1,0,0]),
    vector([1,0,1]),
    vector([1,1,0]),
    vector([1,1,1]),
]
plot(Polyhedron(vertices=corners)) + \
plot(Polyhedron(vertices=[A*c for c in corners]))