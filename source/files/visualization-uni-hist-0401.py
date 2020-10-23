# The following two lines only need to be run once per notebook
# that generates datascience graphics
import matplotlib
%matplotlib inline

# Generate histogram for April 1st
# (Always leave normed=False to measure counts of data values)
pizza_table.where("date","2015-04-01").select("price").hist(bins=20,normed=False)
