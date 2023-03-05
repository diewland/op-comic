import json, os
 
EP_NO = 1
EP_SUPPLY = 100
OUTPUT_DIR = "./json"
START_ID = (EP_SUPPLY * (EP_NO-1)) + 1

NAME = "OP Comic"
DESC = "The OP Comic is a series of 10 Episode (100 each) Hand drawn by Bro_Prins, 95% will donate to RPGF (5% for operation)"
IMG = "https://diewland.github.io/op-comic/assets/Ep01.jpg"
ATTRS = [
    #{
    #  "trait_type": "Edition",
    #  "value": "Special"
    #},
]
ENGINE = "Jigsaw Engine"

tpl = {
  "name": "***",
  "description": DESC,
  "image": IMG,
  "attributes": ATTRS,
  "compiler": ENGINE,
}

for id in range(0, EP_SUPPLY):
    tpl["name"] = "{} EP{} #{}".format(NAME, EP_NO, START_ID+id)
    with open("{}/{}.json".format(OUTPUT_DIR, START_ID+id), "w") as f:
        json.dump(tpl, f)
