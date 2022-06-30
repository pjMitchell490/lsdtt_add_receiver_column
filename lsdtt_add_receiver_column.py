import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='build a vectorized drainage network from LSDTopoTools outputs, divided at tributary junctions.')
parser.add_argument("mChiSegmented", help='LSDTopoTools "*_MChiSegmented.csv" output', type=str)
parser.add_argument("chi_data_map", help='LSDTopoTools "*_chi_data_map.csv" output', type=str)

args = parser.parse_args()
mChiSegmented = pd.read_csv(args.mChiSegmented)
chi_data_map = pd.read_csv(args.chi_data_map)

mChiSegmented['receiver_NI'] = chi_data_map['receiver_NI']

mChiSegmented.to_csv(args.mChiSegmented, index=False)
print("Successfully exported to:", args.mChiSegmented)
