# .plot("datetime") creates a line chart with the datetime column on the
# horizontal axis, and other numerical columns on the vertical axis
pizza_table.select("datetime","price").group("datetime").plot("datetime")
