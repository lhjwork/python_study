import pickle

# 파일을 열어서 profile_file이라는 변수로 불러와서 print 해줌
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
