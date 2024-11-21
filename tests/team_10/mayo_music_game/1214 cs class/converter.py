new_notes = []
new_times = []
current_note = [0, 0, 0, 0]
mode = "perform"

with open(f"D:\\program project\\python_project\\Games\\mayo_music_game\\note_and_time\\osu_{mode}.txt", "r") as osu:
    for i in osu:
        two = False
        time = ""
        comma_count = 0
        if i[0] == "6":
            new_notes.append(64)
        if i[0] == "1":
            new_notes.append(192)
        if i[0] == "3":
            new_notes.append(320)
        if i[0] == "4":
            new_notes.append(448)
        for j in range(len(i)):
            if i[j] == ',':
                comma_count += 1
                two = True
            if comma_count == 2 and not two:
                time += i[j]
            if comma_count >= 3:
                new_times.append(time)
                break
            two = False
            

print(new_notes)
print(new_times)

with open(f"D:\\program project\\python_project\\Games\\mayo_music_game\\note_and_time\\times_{mode}.txt", "a") as f_time:
    for i in new_times:
        f_time.write(i)
        f_time.write("\n")

with open(f"D:\\program project\\python_project\\Games\\mayo_music_game\\note_and_time\\notes_{mode}.txt", "a") as f_note:
    for i in new_notes:
        i = str(i)
        f_note.write(i)
        f_note.write("\n")