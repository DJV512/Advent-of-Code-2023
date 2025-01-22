FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.readlines()

seed_row = data[0]
all_seed_numbers = seed_row.split(": ")[1]
seed_numbers = all_seed_numbers.split(" ")
for i in range(len(seed_numbers)):
    seed_numbers[i] = int(seed_numbers[i].strip())


seed_to_soil_rows = data[3:19]
seed_to_soil_dict = {}
for row in seed_to_soil_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    seed_to_soil_dict[source_start] = (dest_start, length)


soil_to_fertilizer_rows = data[21:34]
soil_to_fertilizer_dict = {}
for row in soil_to_fertilizer_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    soil_to_fertilizer_dict[source_start] = (dest_start, length)

fertilizer_to_water_rows = data[36:58]
fertilizer_to_water_dict = {}
for row in fertilizer_to_water_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    fertilizer_to_water_dict[source_start] = (dest_start, length)

water_to_light_rows = data[60:106]
water_to_light_dict = {}
for row in water_to_light_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    water_to_light_dict[source_start] = (dest_start, length)

light_to_temperature_rows = data[108:134]
light_to_temperature_dict = {}
for row in light_to_temperature_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    light_to_temperature_dict[source_start] = (dest_start, length)

temperature_to_humidity_rows = data[136:158]
temperature_to_humidity_dict = {}
for row in temperature_to_humidity_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    temperature_to_humidity_dict[source_start] = (dest_start, length)

humidity_to_location_rows = data[160:207]
humidity_to_location_dict = {}
for row in humidity_to_location_rows:
    dest_start, source_start, length = row.split(" ")
    dest_start = int(dest_start)
    source_start = int(source_start)
    length = int(length.strip())
    humidity_to_location_dict[source_start] = (dest_start, length)


locations = []
for seed in seed_numbers:
    diff = 999999999999999
    correct_key=""
    for key in seed_to_soil_dict:
        if seed-key < diff and seed-key >= 0 and seed-key <= seed_to_soil_dict[key][1]:
            diff = seed-key
            correct_key = key

    if correct_key == "":
        soil_value = seed
    else:
        value = seed_to_soil_dict[correct_key]
        soil_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in soil_to_fertilizer_dict:
        if soil_value-key < diff and soil_value-key >= 0 and soil_value-key <= soil_to_fertilizer_dict[key][1]:
            diff = soil_value-key
            correct_key = key

    if correct_key == "":
        fertilizer_value = soil_value
    else:
        value = soil_to_fertilizer_dict[correct_key]
        fertilizer_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in fertilizer_to_water_dict:
        if fertilizer_value-key < diff and fertilizer_value-key >= 0 and fertilizer_value-key <= fertilizer_to_water_dict[key][1]:
            diff = fertilizer_value-key
            correct_key = key

    if correct_key == "":
        water_value = fertilizer_value
    else:
        value = fertilizer_to_water_dict[correct_key]
        water_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in water_to_light_dict:
        if water_value-key < diff and water_value-key >= 0 and water_value-key <= water_to_light_dict[key][1]:
            diff = water_value-key
            correct_key = key

    if correct_key == "":
        light_value = water_value
    else:
        value = water_to_light_dict[correct_key]
        light_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in light_to_temperature_dict:
        if light_value-key < diff and light_value-key >= 0 and light_value-key <= light_to_temperature_dict[key][1]:
            diff = light_value-key
            correct_key = key

    if correct_key == "":
        temperature_value = light_value
    else:
        value = light_to_temperature_dict[correct_key]
        temperature_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in temperature_to_humidity_dict:
        if temperature_value-key < diff and temperature_value-key >= 0 and temperature_value-key <= temperature_to_humidity_dict[key][1]:
            diff = temperature_value-key
            correct_key = key

    if correct_key == "":
        humidity_value = temperature_value
    else:
        value = temperature_to_humidity_dict[correct_key]
        humidity_value = value[0]+diff

    diff = 999999999999999
    correct_key=""
    for key in humidity_to_location_dict:
        if humidity_value-key < diff and humidity_value-key >= 0 and humidity_value-key <= humidity_to_location_dict[key][1]:
            diff = humidity_value-key
            correct_key = key

    if correct_key == "":
        location_value = humidity_value
    else:
        value = humidity_to_location_dict[correct_key]
        location_value = value[0]+diff

    print(f"Seed Value = {seed}, Location Value = {location_value}")
    locations.append(location_value)


print(f"Minimum location value = {min(locations)}")