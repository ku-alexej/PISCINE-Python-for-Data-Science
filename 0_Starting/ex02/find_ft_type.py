def all_thing_is_obj(object: any) -> int:

    types = {
        tuple: "Tuple",
        dict: "Dict",
        set: "Set",
        list: "List",
    }

    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (t := type(object)) in types:
        print(f"{types[t]} : {t}")
    else:
        print("Type not found")

    return 42
