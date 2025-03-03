"""

	Code to calculate the outcomes of opening packs in the Cat Bot discord bot.
	Author: @glitchybunny

"""

from main import type_dict, CAT_TYPES, cattypes, pack_data, open_pack
#import random
import csv

def simulate_open_packs(pack_types, n):
	# Test all pack types
	for pack in pack_types:
		# Create CSV with results from pack type
		with open(pack + '.csv', 'w') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(["Starting Pack Level", "Final Pack Level", "Cat Amount", "Cat Type"])

			# Test pack type n times
			for i in range(n):
				result = open_pack(pack)
				writer.writerow(result)

def professor_cat_analyse_pack_results(pack_types):
	# Thou shalt calculate the results of opening packs 
	for pack in pack_types:
		# Count only cats from regular opening (no upgrades)
		open_count = {}
		cat_total = {}
		count = 0

		# Count all cats from opening packs, including when upgrades occur
		upgrade_open_count = {}
		upgrade_cat_total = {}
		upgrade_count = 0

		# Open CSV and count results
		with open(pack + '.csv', 'r') as csv_file:
			reader = csv.reader(csv_file)
			next(reader)
			for row in reader:
				# Count regular pack opens
				if row[0] == row[1]:
					count += 1
					if row[3] in open_count:
						open_count[row[3]] += 1
						cat_total[row[3]] += int(row[2])
					else:
						open_count[row[3]] = 1
						cat_total[row[3]] = int(row[2])

				# Count ALL pack opens (including upgrades)
				upgrade_count += 1
				if row[3] in upgrade_open_count:
					upgrade_open_count[row[3]] += 1
					upgrade_cat_total[row[3]] += int(row[2])
				else:
					upgrade_open_count[row[3]] = 1
					upgrade_cat_total[row[3]] = int(row[2])

		# Print results
		print("\nResults from " + str(upgrade_count) + " " + pack, "packs:")

		print("No upgrades:")
		for v,k in sorted(((v,k) for k,v in cat_total.items()), reverse=True):
			result_string = "\t" + str(v) + " " + k + " cats"
			result_string += "\t(" + '{:.2f}'.format(upgrade_open_count[k] / upgrade_count * 100) + "% of packs)"
			print(result_string)

		print("\nIncluding upgrades:")
		for v,k in sorted(((v,k) for k,v in upgrade_cat_total.items()), reverse=True):
			result_string = "\t" + str(v) + " " + k + " cats"
			result_string += "\t(" + '{:.2f}'.format(upgrade_open_count[k] / upgrade_count * 100) + "% of packs)"
			print(result_string)

		


if __name__ == '__main__':
	pack_types = ["Gold"] #["Wooden", "Stone", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Celestial"]

	# Generate pack data
	simulate_open_packs(pack_types, 10000)

	# Analyse pack results
	professor_cat_analyse_pack_results(pack_types)
