# Add comments like this throughout that explain how this code works.
points = []
all_upper_count = 0
for trial in range(1,100001):
    all_upper = True
    for _ in range(5):
        next_character = randrange(62)
        if next_character >= 26:
            all_upper = False
    if all_upper:
        all_upper_count += 1
    ex_prob = all_upper_count/trial
    points.append( (trial,ex_prob) )

show(
    line(points, color="blue")+line([(1,0.012969),(100000,0.012969)], color="red"),
    axes_labels=["Trials","Exp. Prob."],
)