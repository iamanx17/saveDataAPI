class saveDataDomain:
    def __init__(self, key, value,id=None, note=None, created_on=None, updated_on=None, user=None):

        self.id = id
        
        if not key:
            raise ValueError("key is a required field")
        self.key = key
        
        if not value:
            raise ValueError('value is a required field')
        self.value = value

        self.note = note
        self.created_on = created_on
        self.updated_on = updated_on
        self.user = user
    

    def to_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'value': self.value,
            'note': self.note,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'user': self.user
        }
    
    @staticmethod
    def from_dict(saveDataDict):
        return saveDataDomain(
            id = saveDataDict.get('id'),
            key = saveDataDict.get('key'),
            value = saveDataDict.get('value'),
            note = saveDataDict.get('note'),
            created_on=saveDataDict.get('created_on'),
            updated_on=saveDataDict.get('updated_on'),
            user= saveDataDict.get('user')
        )