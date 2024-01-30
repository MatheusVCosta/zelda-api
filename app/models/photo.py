class Photo:
    
    def __init__(self, type_photo : str):
        self.__type_photo = type_photo
    
    def savePhoto(self):
        print(f"Salvando foto do {self.__type_photo.teste}")
        