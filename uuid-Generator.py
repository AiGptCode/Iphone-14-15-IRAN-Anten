import uuid

unique_id = uuid.uuid4()
print(unique_id)

unique_id_str = unique_id.hex
print("UUID HEX:", (unique_id_str))
