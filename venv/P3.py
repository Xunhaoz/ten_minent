def rum_time():
    rum_time_list = []

    while time := input("輸入跑 10 公里時間： (直接按 Enter 結束) "):
        try:
            time = int(time)
            rum_time_list.append(time)
        except Exception as e:
            print("產生錯誤", e)

    if len(rum_time_list) > 0:
        print("跑", len(rum_time_list), "次的時間為", sum(rum_time_list) / len(rum_time_list), "分鐘")
    else:
        print("沒有資料")

rum_time()










