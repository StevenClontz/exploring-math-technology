heads = 0
total = 0
points = []

for _ in range(1000):
    # re-arrange the following lines, fixing indentation as needed
    heads = heads + 1
    points.append( (total,ex_prob) )
    if flip == "H":
        ex_prob = heads/total
    total = total + 1
    flip = choice(['H','T'])

show(
    line(points, color="blue")+line([(1,0.5),(1000,0.5)], color="red"),
    axes_labels=["Trials","Exp. Prob."],
    ymin=0,
    ymax=1
)