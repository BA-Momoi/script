import keyboard
import yaml
import time

print("=== Tab顺序录制工具 ===")
print("1. 请点击仿真软件的第一个输入框（起点）")
print("2. 按下 F7 开始录制")
print("3. 按 Tab 键移动到需要填写的空白框，按 F8 记录当前位置")
print("4. 所有位置记录完毕后，按 F9 保存并退出\n")

keyboard.wait('F7')
print("录制开始！当前起点序号为 0")
print("按 Tab 移动，按 F8 记录，按 F9 结束")

tab_counter = 0
recorded_indices = []

def on_tab(e):
    global tab_counter
    tab_counter += 1
    print(f"  → 当前 Tab 序号: {tab_counter}")

keyboard.on_press_key('tab', on_tab, suppress=False)

# 用 lambda 来避免回调函数参数问题
keyboard.add_hotkey('F8', lambda: recorded_indices.append(tab_counter))
# 同时打印记录信息，需要多行 lambda 不太方便，我们可以这样：
# 但 add_hotkey 的回调不能有参数，所以我们用一个不带参数的函数包装
# 更干净的方法是写一个不带参数的函数：
def record_current():
    recorded_indices.append(tab_counter)
    print(f"✓ 已记录第 {len(recorded_indices)} 个位置：Tab序号 {tab_counter}")

# 移除原来的 add_hotkey 行，改成下面这句
keyboard.remove_hotkey('F8')  # 先移除可能残留的旧注册
keyboard.add_hotkey('F8', record_current)

keyboard.wait('F9')
keyboard.unhook_all()
print("录制结束。")

with open('tab_sequence.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(recorded_indices, f)
print(f"共记录 {len(recorded_indices)} 个位置，已保存到 tab_sequence.yaml")