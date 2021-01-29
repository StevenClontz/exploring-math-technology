complex_number = CDF(1,1)

graph = points(
    [CDF(complex_number^power) for power in range(4)],
    xmin=-10,ymin=-10,xmax=10,ymax=10,
    aspect_ratio=1,
    pointsize=30
)

for power in range(4):
    graph+=line([CDF(0),CDF(complex_number^power)])

graph