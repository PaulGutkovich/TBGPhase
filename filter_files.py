import os
import shutil

raw_dir = "raw_data/"
out_dir = "filtered_data/"

for file in os.listdir(raw_dir):
	if file[-1] == ".":
		continue
	if file[3] != "B":
		continue
	if file[8] == "m":
		continue

	# DosBZ-CBsum-Im1-I9-numk12-tperp1.0-alpha0.04-U0.50-filling-2.0-xi100-relax0-SymBr1SY-numI2-dp8
	# 0000000000111111111122222222223333333333444444444455555555556666666666777777777788888888889999
	# 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123

	alpha = file[40:44]
	U = file[46:50]
	band = file[6:8]
	component = file[12:14]
	layer = file[14]

	new_filename = f"sum_{alpha}_{U}_{band}_{component}_{layer}.dat"

	shutil.copyfile(f"{raw_dir}{file}", f"{out_dir}{new_filename}")
