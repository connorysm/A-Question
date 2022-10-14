import pandas as pd

read_file = pd.read_csv (r'Q_GCODE.gcode')
read_file.to_csv (r'gcode_out.csv', index=None)
