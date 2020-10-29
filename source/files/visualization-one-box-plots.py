# First code cell
print("Oct 09 Pizza Prices")
pizza_table.where("date","2015-10-09").select("price").hist(normed=False)
pizza_table.where("date","2015-10-09").select("price").boxplot(vert=False)

# Second code cell
print("Oct 10 Pizza Prices")
pizza_table.where("date","2015-10-10").select("price").hist(normed=False)
pizza_table.where("date","2015-10-10").select("price").boxplot(vert=False)