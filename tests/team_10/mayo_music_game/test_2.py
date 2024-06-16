import pygame
import time
import moviepy.editor as mp
import pandas as pd
import numpy as np

pygame.init()

wn = pygame.display.set_mode((800, 600))

mode = "normal"  
drop_before_arrive = 0.8
pixel_per_second = 565 / drop_before_arrive

# Object & Images
mayo = pygame.image.load("oop-python-nycu/tests/team_10/mayo_music_game/images/note.jpg").convert_alpha()
start_menu = pygame.image.load("oop-python-nycu/tests/team_10/mayo_music_game/images/back.jpg").convert_alpha()
start_button = pygame.image.load("oop-python-nycu/tests/team_10/mayo_music_game/images/start.png").convert_alpha()
miss_img = pygame.image.load("oop-python-nycu/tests/team_10/mayo_music_game/images/miss.png").convert_alpha()  # Load miss images
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.transform.scale(start_button, (295, 70))
mayo = pygame.transform.rotate(mayo, 90)
mayo = pygame.transform.scale(mayo, (100, 50))
miss_img = pygame.transform.scale(miss_img, (100, 100))  # Scale miss images
slot = (125, 30)
white_back = pygame.Rect(0, 0, 800, 600)
border_left_line = pygame.Rect(140, 0, 10, 600)
border_right_line = pygame.Rect(650, 0, 10, 600)
display_pressed1 = pygame.Rect(150, 500, slot[0], slot[1])
display_pressed2 = pygame.Rect(275, 500, slot[0], slot[1])
display_pressed3 = pygame.Rect(400, 500, slot[0], slot[1])
display_pressed4 = pygame.Rect(525, 500, slot[0], slot[1])
music_location = "oop-python-nycu/tests/team_10/mayo_music_game/images/hibana 2.mp3"
track = pygame.mixer.music.load(music_location)
font = pygame.font.Font("freesansbold.ttf", 32)

# Screen
pygame.display.set_caption("hibana_music_game")
pygame.display.set_icon(mayo)

# Files
times_arrive = []
times_drop = []
notes = []
note_dict = {64: 0, 192: 1, 320: 2, 448: 3}
with open(f"oop-python-nycu/tests/team_10/mayo_music_game/note_and_time/hibana time.txt", "r") as time_f:
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)
        times_arrive.append(i)

with open(f"oop-python-nycu/tests/team_10/mayo_music_game/note_and_time/hibana notes.txt", "r") as note_f:
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes.append(i)

for i in times_arrive:
    i -= drop_before_arrive  # dropping rate
    i = round(i, 4)
    times_drop.append(i)

# Video Loading
video = mp.VideoFileClip("oop-python-nycu/tests/team_10/mayo_music_game/video.mp4").resize((800, 600))
video_surface = pygame.Surface((800, 600))

# Load scores
try:
    # 尝试读取 scores.csv 文件
    scores_df = pd.read_csv("scores.csv")
except FileNotFoundError:
    # 如果文件不存在，创建一个新的 DataFrame
    scores_df = pd.DataFrame(columns=["name", "score", "average", "std"])

# Classes
class Note:
    def __init__(self, drop_time, arrive_time, xcor, ycor, block):
        self.drop_time = drop_time
        self.arrive_time = arrive_time
        self.xcor = xcor
        self.ycor = ycor
        self.block = block
        self.hit = False
        self.show = True
        self.missed = False  # Add missed attribute
        self.miss_time = None  # Add miss_time attribute

    def ycor_update(self, time_pass):
        p = time_pass - self.drop_time  # Time passed since the note started dropping
        self.ycor += pixel_per_second * p - (self.ycor + 60)  # Update the y-coordinate

    def check_remove(self, time_pass):
        block_check = keys[self.block]
        time_check = abs(time_pass - self.arrive_time) <= 0.1
        if not self.hit and time_pass - self.arrive_time > 0.1 and self.miss_time is None:  # If the note is not hit and it's past the arrive time
            self.missed = True
            self.miss_time = time_pass  # Record the miss time
        return block_check and time_check

# Functions
def background_display(mouse_pos):
    global started
    global start_time
    global video_playing
    if started and not video_playing:
        draw_back()
    else:
        wn.blit(start_menu, (0, 0))
        wn.blit(start_button, (245, 333))
        if mouse == "down":
            if 245 < mouse_pos[0] < 540 and 333 < mouse_pos[1] < 400:
                video_playing = True
                start_video()

def start_video():
    global video_start_time
    video_start_time = time.time()

def draw_back():
    pygame.draw.rect(wn, (128, 128, 128), white_back)
    pygame.draw.rect(wn, (128, 0, 128), border_left_line)
    pygame.draw.rect(wn, (128, 0, 128), border_right_line)
    
    pygame.draw.line(wn, (255, 255, 255), (275, 0), (275, 600))
    pygame.draw.line(wn, (255, 255, 255), (400, 0), (400, 600))
    pygame.draw.line(wn, (255, 255, 255), (525, 0), (525, 600))
    
    pygame.draw.line(wn, (0, 0, 0), (150, 500), (650, 500))
    pygame.draw.line(wn, (0, 0, 0), (150, 530), (650, 530))

def draw_press():
    if keys[pygame.K_d]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed1)
    if keys[pygame.K_f]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed2)
    if keys[pygame.K_j]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed3)
    if keys[pygame.K_k]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed4)

def pre_time_handle():
    global loop_start_time
    global start_time
    global time_pass
    loop_start_time = time.time()
    if not started:
        start_time = loop_start_time
    time_pass = float(loop_start_time - start_time)
    time_pass = round(time_pass, 4)

def post_time_handle(loop_start_time):
    now_end_time = time.time()
    now_end_time = round(now_end_time, 4)
    loop_time = now_end_time - loop_start_time
    if loop_time < 0.001:
        time.sleep(0.001 - loop_time)

def note_remove(time_pass):
    for one_note in showing_array:
        if one_note.check_remove(time_pass):
            one_note.hit = True
            one_note.show = False

def showingArray_appending(time_pass):
    global showing_array
    global pointer
    coresponding_location = [160, 285, 410, 535]
    coresponding_key = {0: pygame.K_d, 1: pygame.K_f, 2: pygame.K_j, 3: pygame.K_k}
    while pointer < len(times_drop) and abs(time_pass - times_drop[pointer]) <= 0.1:
        one_note = Note(times_drop[pointer], times_arrive[pointer], coresponding_location[notes[pointer]], -100, coresponding_key[notes[pointer]])
        showing_array.append(one_note)
        pointer += 1

def note_displaying(time_pass):
    global showing_array
    for one_note in showing_array:
        if one_note.show:
            one_note.ycor_update(time_pass)
            wn.blit(mayo, (one_note.xcor, one_note.ycor))
        if one_note.missed and not one_note.hit and one_note.show:
            wn.blit(miss_img, (one_note.xcor, 500))  # Display the miss image at the judgment line
        if one_note.ycor >= 900:  # Note goes off-screen
            one_note.show = False

def combo_showing():
    global combo
    combo = 0
    note_died_count = 0
    global max_combo

    for one_note in showing_array:
        if one_note.arrive_time < time_pass:
            note_died_count += 1
    for i in range(note_died_count):
        if showing_array[i].hit:
            combo += 1
            if combo > max_combo:
                max_combo = combo
        else:
            combo = 0

    combo_show = font.render(f"COMBO: {combo}", True, (255, 255, 255))
    wn.blit(combo_show, (10, 10))

def check_game_over():
    if pointer >= len(times_drop) and all(not note.show for note in showing_array):
        return True
    return False

def show_game_over_screen():
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    wn.blit(game_over_text, (300, 250))
    pygame.display.flip()
    time.sleep(5)  # Show the game over screen for 5 seconds

def pygame_events():
    global running
    global mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""

# Global Variables
running = True
mouse = ""
pointer = 0
start_time = 0
started = False
video_playing = False
showing_array = []
time_pass = 0
combo = 0
max_combo = 0
showing_pointer = 0
game_over = False

# Main process
while running:
    if game_over:
        show_game_over_screen()
        break
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    pygame_events()
    pre_time_handle()
    
    if video_playing:
        current_time = time.time() - video_start_time
        if current_time < video.duration:
            video_frame = video.get_frame(current_time)
            video_surface = pygame.surfarray.make_surface(video_frame.swapaxes(0, 1))
            video_surface = pygame.transform.scale(video_surface, (800, 600))
            wn.blit(video_surface, (0, 0))
        else:
            video_playing = False
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
            started = True
            start_time = time.time()
    else:
        background_display(mouse_pos)
        draw_press()
        note_remove(time_pass)
        showingArray_appending(time_pass)
        note_displaying(time_pass)
        combo_showing()
        
    if check_game_over():
        game_over = True
    
    pygame.display.update()
    post_time_handle(loop_start_time)

pygame.quit()

# Save the score
name = input("Enter your name: ")

# 检查用户是否已经存在于 scores_df 中
if name in scores_df["name"].values:
    # 获取当前用户的所有记录
    current_record = scores_df[scores_df["name"] == name]
    current_score = current_record["score"].values[0]
    current_average = current_record["average"].values[0]
    current_plays = current_record["plays"].values[0]

    # 更新用户的最高成绩
    if max_combo > current_score:
        scores_df.loc[scores_df["name"] == name, "score"] = max_combo

    # 更新用户的游玩次数
    new_plays = current_plays + 1
    scores_df.loc[scores_df["name"] == name, "plays"] = new_plays

    # 计算新的平均成绩并更新
    new_average = (current_average * current_plays + max_combo) / new_plays
    scores_df.loc[scores_df["name"] == name, "average"] = new_average

    # 获取当前用户的所有分数，并添加当前分数
    user_scores = current_record["score"].tolist() * int(current_plays) + [max_combo]
    # 计算用户的标准差并更新
    std_score = np.std(user_scores, ddof=0)  # ddof=0 计算总体标准差
    scores_df.loc[scores_df["name"] == name, "std"] = std_score
else:
    # 添加新的分数记录并计算平均值和标准差
    new_score = pd.DataFrame({
        "name": [name], 
        "score": [max_combo], 
        "average": [max_combo],
        "std": [0.0],  # 只有一个分数，标准差为0
        "plays": [1]  # 新用户的游玩次数为1
    })
    scores_df = pd.concat([scores_df, new_score], ignore_index=True)

# 显示结果
scores_df.index = scores_df.index + 1
print(scores_df)

# 保存结果到 scores.csv
scores_df.to_csv("scores.csv", index=False)