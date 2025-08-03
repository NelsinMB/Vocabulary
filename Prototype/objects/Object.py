import json

class Object:
    def __init__(self, id, name, type, metadata):
        self.id = id
        self.name = name
        self.type = type
        self.metadata = json.loads(metadata) # Not sure what I will use this for yet.  