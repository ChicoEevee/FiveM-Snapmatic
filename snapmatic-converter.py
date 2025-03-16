import os
from pathlib import Path

home_directory = os.path.join(str(Path.home()) + "\\Saved Games\\CitizenFX\\GTA5")

for count, pgta in enumerate(os.listdir(home_directory)):    
    if pgta.startswith("PGTA"):
        if os.path.exists(pgta + ".jpg") == False:
            print(pgta)
            photo = open(os.path.join(home_directory, pgta), "rb")
        
            image_data = bytearray()
        
            for i in range(292, os.path.getsize(os.path.join(home_directory, pgta))):
                photo.seek(i)
                image_data += photo.read(1)
            
            out_photo = open(pgta + ".jpg", "wb")
            out_photo = out_photo.write(image_data)
            photo.close()
print("Todas las imagenes fueron convertidas")
