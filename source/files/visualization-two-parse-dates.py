# converts `date` string into a native datetime format
from datetime import datetime
pizza_table = pizza_table.with_column("datetime",pizza_table.apply(
    lambda x:datetime.strptime(x,"%Y-%m-%d"),"date"
))
