class DatabaseConnectionManager:
    __connectionManager = None
    def __init__(self):
        if not DatabaseConnectionManager.__connectionManager:
            print("Constructor called")
        else:
            print("Instance already exists..", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DatabaseConnectionManager()
        return cls.__connectionManager

    def connect(self):
        pass


    def disconnect(self):
        pass
