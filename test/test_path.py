# 字符串路径（需手动用os.path.join适配）
import os
path1 = os.path.join("D:", "test", "pdf.pdf")  # Windows→D:\test\pdf.pdf，Linux→D:/test/pdf.pdf
print(path1)

# Path对象（自动适配，更简洁）
# 路径拼接更直观，支持「/」运算符
from pathlib import Path
path2 = Path("D:") / "test" / "pdf.pdf"  # 用/直接拼接，自动适配系统分隔符
print(path2)

# Path 封装了路径的「属性」，直接获取路径信息，无需手动解析
p = Path("D:/test/report_v1.2.pdf")
print(p.name)      # 获取完整文件名：report_v1.2.pdf
print(p.stem)      # 获取文件纯名称（无后缀）：report_v1.2（你代码中核心使用的属性）
print(p.suffix)    # 获取文件后缀：.pdf
print(p.parent)    # 获取父目录：D:/test
print(p.absolute())# 获取绝对路径：D:\test\report_v1.2.pdf（Windows）


# Path 封装了路径的「操作方法」，直接调用，无需传参
p = Path("D:/test.pdf")
d = Path("D:/output")

# Path对象（直接调用方法）
p.exists()    # 判断路径是否存在，等价于os.path.exists(p)
p.is_file()   # 判断是否是文件，等价于os.path.isfile(p)
d.mkdir(parents=True, exist_ok=True)  # 创建目录，等价于os.makedirs(d, exist_ok=True)

# 字符串路径+os.path（需传参，繁琐）
import os
os.path.exists(str(p))
os.path.isfile(str(p))
os.makedirs(str(d), exist_ok=True)

# 与 Python 内置函数无缝兼容，无需频繁类型转换
p = Path("D:/test.md")
# 直接传入Path对象，无需str(p)
with open(p, "r", encoding="utf-8") as f:
    content = f.read()

# 字符串路径（需直接传字符串）
with open(str(p), "r", encoding="utf-8") as f:
    content = f.read()
