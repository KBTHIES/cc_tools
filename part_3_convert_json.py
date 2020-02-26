#Part 3
#Load your custom JSON file
import json
import cc_dat_utils
import cc_classes
#Open the file specified by input_json_file
input_json_file = "data/kthies_cc1.json"
with open(input_json_file) as json_file:
    #Use the json module to load the data from the file
    json_data = json.load(json_file)

#Convert JSON data to CCLevelPack
new_level_pack = cc_classes.CCLevelPack
new_level_pack.__init__(new_level_pack)
print(new_level_pack.levels)
for json_level in json_data["levels"]:
    new_level = cc_classes.CCLevel
    new_level.__init__(new_level)
    new_level.level_number = json_level["level number"]
    new_level.time = json_level["time"]
    new_level.num_chips = json_level["chips"]
    new_level.upper_layer = json_level["upper layer"]
    new_level.optional_fields = []

    for json_field in json_level["optional fields"]:
        field_type = json_field["field type"]
        if field_type == "title":
            new_title_field = cc_classes.CCMapTitleField(json_field["title"])
            new_level.add_field(new_level, new_title_field)
        elif field_type == "hint":
            new_hint_field = cc_classes.CCMapHintField(json_field["hint"])
            new_level.add_field(new_level, new_hint_field)
        elif field_type == "password":
            new_password_field = cc_classes.CCEncodedPasswordField(json_field["password"])
            new_level.add_field(new_level, new_password_field)
        elif field_type == "monsters":
            monsters = []
            for json_monster in json_field["monsters"]:
                x = json_monster["x"]
                y = json_monster["y"]
                new_monster_coord = cc_classes.CCCoordinate(x, y)
                monsters.append(new_monster_coord)
            new_monster_field = cc_classes.CCMonsterMovementField(monsters)
            new_level.add_field(new_level, new_monster_field)
        new_level_pack.add_level(new_level_pack, new_level)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/kthies_cc1.dat")
test_dat = cc_dat_utils.make_cc_level_pack_from_dat("data/kthies_cc1.dat")
print(test_dat)