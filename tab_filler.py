import pandas as pd
import yaml
import pyautogui
import time
import keyboard

# ---------- 配置区 ----------
EXCEL_FILE = '误差.xlsx'
SHEET_NAME = 'Sheet1'
SEQ_FILE = 'tab_sequence.yaml'

# ---------- 读取数据 ----------
df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, header=None)
values = []
for row in df.itertuples(index=False):
    for cell in row:
        if pd.notna(cell):
            values.append(cell)

print(f"从 Excel 读取到 {len(values)} 个待填值")

# ---------- 读取 Tab 序号 ----------
with open(SEQ_FILE, 'r', encoding='utf-8') as f:
    indices = yaml.safe_load(f)

if len(values) != len(indices):
    print(f"⚠ 警告：数据个数({len(values)})与记录的位置个数({len(indices)})不匹配！")
    print("将按较短的长度填写")
    min_len = min(len(values), len(indices))
    values = values[:min_len]
    indices = indices[:min_len]

print("读取到的填写序号顺序:", indices)

print("\n请手动点击仿真软件的第一个输入框（与录制时相同的起点），然后按下 F10 开始...")
keyboard.wait('F10')
time.sleep(0.5)

pyautogui.FAILSAFE = True
current_index = 0

for i, (target_index, value) in enumerate(zip(indices, values)):
    diff = target_index - current_index
    if diff < 0:
        print(f"错误：目标序号 {target_index} 小于当前序号 {current_index}，录制顺序有误")
        break

    print(f"\n[{i+1}] 按 Tab {diff} 次到达序号 {target_index}...")
    for _ in range(diff):
        pyautogui.press('tab')
        time.sleep(0.05)
    current_index = target_index

    s = str(value)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write(s, interval=0.02)
    time.sleep(0.15)
    print(f"  已填入: {s}")

print("\n全部填写完毕！")