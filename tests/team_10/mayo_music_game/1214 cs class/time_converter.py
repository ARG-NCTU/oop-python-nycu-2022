times = []
mode = "perform"
with open(f"D:\\program project\\python_project\\Games\\mayo_music_game\\note_and_time\\times_{mode}.txt", "r") as f_time:
    for i in f_time:
        times.append(int(i) + 180)
with open(f"D:\\program project\\python_project\\Games\\mayo_music_game\\note_and_time\\times_{mode}.txt", "w") as f_time:
    for i in times:
        f_time.write(str(i))
        f_time.write("\n")