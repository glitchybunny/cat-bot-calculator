"""

	Code to calculate the outcomes of opening packs in the Cat Bot discord bot.
	Author: @glitchybunny

"""

from main import type_dict, CAT_TYPES, cattypes, pack_data
import random
import csv

def open_pack(pack):
	level = next((i for i, p in enumerate(pack_data) if p["name"] == pack), 0)

	# bump rarity
	try_bump = True
	while try_bump:
		if random.randint(1, 100) <= pack_data[level]["upgrade"]:
			level += 1
		else:
			try_bump = False
	final_level = pack_data[level]

	# select cat type
	goal_value = final_level["value"]
	lower_bound, upper_bound = goal_value * 0.85, goal_value * 1.15
	found = []
	while not found:
		test_type = random.choice(cattypes)
		value_per_type = len(CAT_TYPES) / type_dict[test_type]
		n = 0
		while True:
			n += 1
			if value_per_type * n < lower_bound:
				continue
			if value_per_type * n > upper_bound:
				break
			found.append([test_type, n])
	reward = random.choice(found)

	# return starting pack level, final pack level, cat amount and type
	return (pack, final_level['name'], reward[1], reward[0])

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
	# 
	for pack in pack_types:
		type_count = {}
		type_total = {}
		total_count = 0

		# Open CSV and count results
		with open(pack + '.csv', 'r') as csv_file:
			reader = csv.reader(csv_file)
			next(reader)
			for row in reader:
				total_count += 1
				if row[3] in type_count:
					type_count[row[3]] += 1
					type_total[row[3]] += int(row[2])
				else:
					type_count[row[3]] = 1
					type_total[row[3]] = int(row[2])

		# Print results
		print("\nResults for opening " + str(total_count) + " " + pack, "packs:")
		for cat_total,cat_type in sorted(((v,k) for k,v in type_total.items()), reverse=True):
			result_string = str(cat_total) + " " + cat_type + " cats"
			result_string += "\t(" + '{:.2f}'.format(type_count[cat_type] / total_count * 100) + "% of packs)"
			print(result_string)


if __name__ == '__main__':
	pack_types = ["Gold"] #["Wooden", "Stone", "Bronze", "Silver", "Gold"]

	# Generate pack data
	simulate_open_packs(pack_types, 100000)

	# Analyse pack results
	professor_cat_analyse_pack_results(pack_types)
