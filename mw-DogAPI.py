import json, os, sys, urllib, urllib as urlrequest, urlparse
from random import randint
from PIL import Image
class dog_API(object):
    def api_Request(self, api_URL):
        return json.loads(urlrequest.urlopen(urlparse.urljoin("https://dog.ceo/api/", api_URL)).read())
    def list_Breeds(self):
        all_Breeds = self.api_Request("breeds/list")["message"]
        for dog in all_Breeds:
            print dog
            sub_Breeds = self.api_Request("breed/{}/list".format(dog))["message"]
            if sub_Breeds is not None:
                for breed in sub_Breeds:
                    print breed, dog
        return dog_API().menu()
    def pick_Breed(self):
        user_Choice = raw_input("Type a breed to display a list of subbreeds: ")
        sub_Breeds = self.api_Request("breed/{}/list".format(user_Choice))["message"]
        if sub_Breeds == "Breed not found":
            print "Breed not found, try again."
            dog_API().pick_Breed()
        else:
            for sub_Breed in sub_Breeds:
                print sub_Breed, user_Choice
        return dog_API().menu()
    def random_Picture(self):
        picture_URL = self.api_Request("breeds/image/random")["message"]
        picture_Name = "random-dog-"+str(randint(1000,9999))+".jpg"
        image = urllib.URLopener()
        image.retrieve(picture_URL, picture_Name)
        print "Image stored at:",os.getcwd()+picture_Name
        image = Image.open(picture_Name)
        image.show()
        dog_API().menu()
    def breed_Picture(self):
        user_Choice = raw_input("Type a breed to download a random picture of that breed: ")
        picture_URL = self.api_Request("breed/{}/images/random".format(user_Choice))["message"]
        if picture_URL == "Breed not found":
            print "Breed not found, try again."
            dog_API().breed_Picture()
        else:
            picture_Name = user_Choice+"-"+str(randint(1000,9999))+".jpg"
            image = urllib.URLopener()
            image.retrieve(picture_URL, picture_Name)
            print "Image stored at:",os.getcwd()+"/"+picture_Name
            image = Image.open(picture_Name)
            image.show()
            return dog_API().menu()
    def menu(self):
        user_Choice = raw_input("\nMenu:\n1. List all dog breeds and subbreeds.\n2. Discover subbreeds.\n3. Download and display a random dog picture.\n4. Download and dislpay picture of a certain breed.\n5. Quit.\nChoose an option: ")
        if user_Choice == "1":
            dog_API().list_Breeds()
        elif user_Choice == "2":
            dog_API().pick_Breed()
        elif user_Choice == "3":
            dog_API().random_Picture()
        elif user_Choice == "4":
            dog_API().breed_Picture()
        elif user_Choice == "5":
            return
        else:
            dog_API().menu()
dog_API().menu()