import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image

class ImageCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("画像圧縮ツール")
        self.root.geometry("400x200")  # ウィンドウサイズを変更

        self.selected_folder = tk.StringVar()

        # 参照フォルダ選択
        self.folder_frame = tk.Frame(root)
        self.folder_frame.pack(pady=10)

        self.folder_label = tk.Entry(self.folder_frame, textvariable=self.selected_folder)
        self.folder_label.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.select_folder_button = tk.Button(self.folder_frame, text="参照", command=self.select_folder)
        self.select_folder_button.pack(side=tk.RIGHT, padx=5)

        # テキストボックスの幅を広げる
        self.folder_label.config(width=30)

        # リサイズパーセンテージ入力
        self.resize_label = tk.Label(root, text="リサイズパーセンテージ（%）:")
        self.resize_label.pack()
        self.resize_entry = tk.Entry(root)
        self.resize_entry.pack()

        # 圧縮実行ボタン
        self.compress_button = tk.Button(root, text="圧縮開始", command=self.compress_images)
        self.compress_button.pack(pady=10)

        # 進捗バー
        self.progress = Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.selected_folder.set(folder_path)

    def compress_images(self):
        folder_path = self.selected_folder.get()
        if not folder_path:
            messagebox.showerror("エラー", "フォルダが選択されていません。")
            return
        try:
            resize_percentage = float(self.resize_entry.get())
            compressed_folder = os.path.join(folder_path, "圧縮画像")
            if not os.path.exists(compressed_folder):
                os.makedirs(compressed_folder)
            image_files = [filename for filename in os.listdir(folder_path)
                           if filename.endswith((".jpg", ".png"))]
            num_images = len(image_files)
            self.progress["maximum"] = num_images
            for index, filename in enumerate(image_files, start=1):
                image_path = os.path.join(folder_path, filename)
                with Image.open(image_path) as img:
                    width, height = img.size
                    new_width = int(width * (resize_percentage / 100))
                    new_height = int(height * (resize_percentage / 100))
                    resized_img = img.resize((new_width, new_height))
                    output_path = os.path.join(compressed_folder, filename)
                    resized_img.save(output_path)
                self.progress["value"] = index
                self.root.update_idletasks()
            messagebox.showinfo("完了", "画像の圧縮が完了しました。")
        except Exception as e:
            messagebox.showerror("エラー", f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()
