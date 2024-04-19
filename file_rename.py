import os
import tkinter as tk
from tkinter import filedialog

def replace_filenames(folder_path, old_text, new_text):
    try:
        # 指定されたフォルダ内のファイル一覧を取得
        files = os.listdir(folder_path)
        for file in files:
            # ファイル名に古いテキストが含まれている場合、置換してリネームする
            if old_text in file:
                new_file = file.replace(old_text, new_text)
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file))
        print("ファイル名の置換が完了しました。")
    except Exception as e:
        print("エラーが発生しました:", e)

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def replace_names():
    folder_path = folder_entry.get()
    old_text = old_entry.get()
    new_text = new_entry.get()
    replace_filenames(folder_path, old_text, new_text)

# GUIの作成
root = tk.Tk()
root.title("ファイル名置換ツール")

# フォルダ選択部分
folder_label = tk.Label(root, text="フォルダ:")
folder_label.grid(row=0, column=0, padx=5, pady=5)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
folder_button = tk.Button(root, text="参照", command=select_folder)
folder_button.grid(row=0, column=2, padx=5, pady=5)

# 置換前テキスト入力部分
old_label = tk.Label(root, text="置換前のテキスト:")
old_label.grid(row=1, column=0, padx=5, pady=5)
old_entry = tk.Entry(root, width=50)
old_entry.grid(row=1, column=1, padx=5, pady=5)

# 置換後テキスト入力部分
new_label = tk.Label(root, text="置換後のテキスト:")
new_label.grid(row=2, column=0, padx=5, pady=5)
new_entry = tk.Entry(root, width=50)
new_entry.grid(row=2, column=1, padx=5, pady=5)

# ボタン
replace_button = tk.Button(root, text="ファイル名置換", command=replace_names)
replace_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
