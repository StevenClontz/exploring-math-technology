# The backslash can be used to continue a long line on multiple lines
testing_table.where("PlcmtScore",are.above(0)).where("SATM",are.above(0)) \
    .select("SATM","PlcmtScore").scatter("SATM")