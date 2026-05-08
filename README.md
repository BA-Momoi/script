# 一个居于Python记录tab次数并输出的py脚本
> [!IMPORTANT]
> python版本建议为3.12
> 且首次运行前请先安装pandas openpyxl pyautogui keyboard pyyaml依赖
```Py
* 适配Py3.12的一键安装命令 *
* python -m pip install pandas==2.2.3 openpyxl pyautogui keyboard pyyaml *
```
## 首次执行前请先将所需xlsx文件导入至脚本相同目录

 ``` Python
 * 位于tab_filler.py文件 *
* EXCEL_FILE = '误差.xlsx' //将''内修改为你的xlsx文件
  SHEET_NAME = 'Sheet1' //一般不需要动
  SEQ_FILE = 'tab_sequence.yaml' //生成的脚本配置文件名称 *
  ```
  #### 在运行脚本时建议cd 至脚本目录，不然tab_recorder生成的配置文件会在你所在目录，而非脚本目录
  - ## 再是执行tab_recorder.py，根据提示执行，录制结束后按F9结束录制并保存生成tab_sequence.yaml文件
  - ## 有了脚本配置文件，再是执行tab_filler.py脚本，根据提示开始
  > [!WARNING]  
  > 在执行脚本时请切换为英文输入法，中文输入法可能使脚本> 无法正确换行