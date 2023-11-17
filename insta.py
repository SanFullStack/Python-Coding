import instaloader
obj=instaloader.Instaloader()
user=input("Enter the name:")
obj.download_profile(user,profile_pic_only=True)