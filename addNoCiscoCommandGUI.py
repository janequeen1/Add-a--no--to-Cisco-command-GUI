import tkinter as tk
from tkinter import messagebox

# 명령어에 'no'를 붙이는 함수
def add_no_to_command():
    command = text_input.get("1.0", tk.END).strip()  # 입력 텍스트를 가져옴
    if not command:
        messagebox.showwarning("경고", "명령어를 입력해주세요!")
        return

    # 각 줄에 'no'를 붙임
    no_commands = '\n'.join([f"no {line.strip()}" for line in command.splitlines()])
    
    # 결과 창에 표시
    text_output.delete("1.0", tk.END)  # 기존 텍스트 제거
    text_output.insert(tk.END, no_commands)

# UI 초기 설정
root = tk.Tk()
root.title("Cisco Command Modifier")

# 입력 프레임
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_input = tk.Label(frame_input, text="명령어 입력:")
label_input.pack(anchor="w")

text_input = tk.Text(frame_input, height=10, width=50)
text_input.pack()

# 출력 프레임
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_output = tk.Label(frame_output, text="no가 붙은 명령어:")
label_output.pack(anchor="w")

text_output = tk.Text(frame_output, height=10, width=50)
text_output.pack()

# 변환 버튼
convert_button = tk.Button(root, text="no 붙이기", command=add_no_to_command)
convert_button.pack(pady=10)

# UI 실행
root.mainloop()
