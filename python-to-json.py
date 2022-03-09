#conversion of python to json
import json
abc={
    "fname":"pravallika",
    "lname":"nalamothu",
    "age":22,
    "city":"ongole"

}

con_json=json.dumps(abc)
print(con_json)