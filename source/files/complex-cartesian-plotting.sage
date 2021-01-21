# Example list of complex numbers
complex_list = [3, 4-2*CDF(I), CDF(-1,5)]

# Plot complex_list in the plane
points(
    [CDF(x) for x in complex_list],
    xmin=-6,ymin=-6,xmax=6,ymax=6,
    aspect_ratio=1,
    pointsize=30
)