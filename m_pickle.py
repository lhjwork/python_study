import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장

profile_file.close()
