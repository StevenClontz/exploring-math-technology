def with_correlated_columns(self,num_rows=100,x_range=5,slope=1,noise=1):
    from random import random
    table = self.select().with_columns("x",[],"y",[])
    for _ in range(num_rows):
        seed = random()
        x = seed*x_range
        y = seed*x_range*slope
        y = y + (-1+2*random())*noise
        table = table.with_row([x,y])
    return table
def correlation(self,col1_name,col2_name):
    import statistics
    # get column arrays
    col1 = self.column(col1_name)
    col2 = self.column(col2_name)
    # standardize units
    col1_s = (col1 - statistics.mean(col1))/statistics.stdev(col1)
    col2_s = (col2 - statistics.mean(col2))/statistics.stdev(col2)
    # correlation is the mean product of standard units
    return statistics.mean(col1_s*col2_s)
setattr(Table,"with_correlated_columns",with_correlated_columns)
setattr(Table,"correlation",correlation)