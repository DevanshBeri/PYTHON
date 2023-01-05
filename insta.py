import instaloader
ig=instaloader.Instaloader()

dp=input("Enter your username\n\n")

ig.download_profile(dp,profile_pic_only=True)
