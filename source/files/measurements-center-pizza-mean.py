# FIXME
# this code says the mean cost of a pizza is less than a dollar!
prices = pizza_table.where("date","2015-10-09").column("price")
len(prices)/sum(prices)
