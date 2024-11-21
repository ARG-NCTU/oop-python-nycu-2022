times = []
old_notes = []
new_notes = []
with open("D:\program project\python_project\Games\mayo_music_game\\times.txt", "r") as f_time:
    for i in f_time:
        i = int(i)
        times.append(i)
with open("D:\program project\python_project\Games\mayo_music_game\\notes.txt", "r") as f_note:
    for i in f_note:
        i = int(i)
        old_notes.append(i)

pointer = 0

for i in range(len(times)):
    if(times[pointer]):
        pass
