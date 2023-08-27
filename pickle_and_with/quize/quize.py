for i in range(1, 51):
    with open(
        f"C:/Users/jinco/OneDrive/Desktop/projects/python/pickle_and_with/quize/result/{i} 주차 주간보고.txt",
        "w",
        encoding="utf8",
    ) as report:
        lines = [f"-{i} 주차 주간보고 -\n", "부서 : \n", "이름 : \n", "업무 요약 : \n"]
        report.writelines(lines)
