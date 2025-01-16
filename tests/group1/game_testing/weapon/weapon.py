import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

#print(PIL.__version__)  # 打印版本以確認安裝正確

# 假設的裝備數據庫(temprary)
GEAR_DATA = {
    "武器": {
        "sword": ["劍", "攻擊力: 50", "images/weapon_sword.png"],
        "axe": ["斧頭", "攻擊力: 70", "images/weapon_axe.png"],
    },
    "裝甲": {
        "shield": ["盾牌", "防禦力: 30", "images/armor_shield.png"],
        "helmet": ["頭盔", "防禦力: 20", "images/armor_helmet.png"],
    },
    "符文": {
        "fire_rune": ["火符文", "加強火屬性攻擊", "images/rune_fire.png"],
        "ice_rune": ["冰符文", "加強冰屬性攻擊", "images/rune_ice.png"],
    },
}

class EquipmentSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("遊戲角色裝備配置介面")
        self.geometry("600x400")

        # 初始化選擇
        self.selected_gear = {"武器": None, "裝甲": None, "符文": None}

        # 建立介面
        self.create_widgets()

    def create_widgets(self):
        row = 0
        for category, items in GEAR_DATA.items():
            tk.Label(self, text=category, font=("Arial", 16)).grid(row=row, column=0, padx=10, pady=10, sticky="w")

            # 下拉選單
            gear_var = tk.StringVar()
            combo = ttk.Combobox(self, textvariable=gear_var, state="readonly")
            combo["values"] = list(items.keys())
            combo.grid(row=row, column=1, padx=10, pady=10)

            # 顯示裝備資訊
            display_button = tk.Button(self, text="顯示資訊", command=lambda c=category, gv=gear_var: self.display_info(c, gv))
            display_button.grid(row=row, column=2, padx=10, pady=10)

            # 設定選擇按鈕
            select_button = tk.Button(self, text="選擇", command=lambda c=category, gv=gear_var: self.select_gear(c, gv))
            select_button.grid(row=row, column=3, padx=10, pady=10)

            row += 1

        # 完成按鈕
        complete_button = tk.Button(self, text="完成選擇", command=self.complete_selection)
        complete_button.grid(row=row, column=0, columnspan=4, pady=20)

    def display_info(self, category, gear_var):
        gear_key = gear_var.get()
        if gear_key in GEAR_DATA[category]:
            gear_info = GEAR_DATA[category][gear_key]
            image_path = gear_info[2]

            try:
                img = Image.open(image_path)
                img = img.resize((100, 100))
                img = ImageTk.PhotoImage(img)

                # 創建一個新窗口顯示裝備圖片
                info_window = tk.Toplevel(self)
                info_window.title(f"{gear_info[0]} 資訊")
                
                tk.Label(info_window, text=f"名稱: {gear_info[0]}").pack(pady=10)
                tk.Label(info_window, text=f"描述: {gear_info[1]}").pack(pady=10)
                tk.Label(info_window, image=img).pack(pady=10)
                info_window.img = img  # 防止垃圾回收

            except FileNotFoundError:
                messagebox.showerror("錯誤", f"無法找到圖片: {image_path}")
        else:
            messagebox.showwarning("警告", "請先選擇裝備！")

    def select_gear(self, category, gear_var):
        gear_key = gear_var.get()
        if gear_key in GEAR_DATA[category]:
            self.selected_gear[category] = GEAR_DATA[category][gear_key]
            messagebox.showinfo("成功", f"已選擇 {category}: {GEAR_DATA[category][gear_key][0]}")
        else:
            messagebox.showwarning("警告", "請先選擇裝備！")

    def complete_selection(self):
        if all(self.selected_gear.values()):
            summary = "\\n".join([f"{cat}: {gear[0]} ({gear[1]})" for cat, gear in self.selected_gear.items()])
            messagebox.showinfo("選擇完成", f"你已選擇:\\n{summary}")
        else:
            messagebox.showwarning("警告", "請確認所有裝備都已選擇！")

if __name__ == "__main__":
    # 確保圖片資料夾存在並放置圖片
    if not os.path.exists("images"):
        os.makedirs("images")

    app = EquipmentSelector()
    app.mainloop()
