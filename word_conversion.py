import tkinter as tk


def replace_text():
    original_text = text_input.get("1.0", "end-1c")
    original_word = original_word_input.get()
    replacement_word = replacement_word_input.get()

    if not original_text.strip():  # 置換対象のテキストが空の場合、エラーメッセージを表示
        text_output.delete("1.0", "end")
        text_output.insert("1.0", "Error: 置換対象のテキストが空です。")
    elif not original_word:  # 置換前の用語が入力されていない場合、エラーメッセージを表示
        text_output.delete("1.0", "end")
        text_output.insert("1.0", "Error: 置換前の用語を入力してください。")
    else:
        replaced_text = original_text.replace(original_word, replacement_word)
        text_output.delete("1.0", "end")
        text_output.insert("1.0", replaced_text)


def clear_text():
    text_input.delete("1.0", "end")
    text_output.delete("1.0", "end")
    original_word_input.delete(0, "end")
    replacement_word_input.delete(0, "end")


# GUIの設定
root = tk.Tk()
root.title("テキスト置換ツール")
root.geometry("600x500")  # ウィンドウの初期サイズを設定

# 対象のテキスト
text_label = tk.Label(root, text="置換対象のテキスト")
text_label.pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# 置換前の用語
original_word_label = tk.Label(root, text="置換前の用語")
original_word_label.pack()
original_word_input = tk.Entry(root)
original_word_input.pack()

# 置換後の用語
replacement_word_label = tk.Label(root, text="置換後の用語")
replacement_word_label.pack()
replacement_word_input = tk.Entry(root)
replacement_word_input.pack()

# 置換ボタン
replace_button = tk.Button(root, text="テキストを置換", command=replace_text)
replace_button.pack()

# 置換結果の表示
text_output_label = tk.Label(root, text="置換後のテキスト")
text_output_label.pack()
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

# テキストクリアボタン
clear_button = tk.Button(root, text="テキストをクリア", command=clear_text)
clear_button.pack(pady=5)  # ボタンを少し離す

root.mainloop()
