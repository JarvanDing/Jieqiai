# 完整稳定版本

这个文件夹包含项目中最完整、最稳定的版本，适合用于生产环境或继续开发。

## Python版本

**位置**: `python/`

### 主引擎
- `musesfish_pvs_20210604_fixed.py` - 最完整的稳定版本

这是Python版本中最完整的稳定版本，包含：
- 修复了calc_average函数的重大BUG
- 引入有根子和静态搜索(Quiescence)
- 将空头炮逻辑写为静态逻辑
- 支持pypy3运行以获得更好性能

### GUI界面
- `gui.py` - 图形界面（使用pygame）

### 运行方法

**命令行版本**:
```bash
cd python
python musesfish_pvs_20210604_fixed.py
# 或使用pypy3获得更好性能
pypy3 musesfish_pvs_20210604_fixed.py
```

**GUI版本**:
```bash
cd python
python gui.py
```

### 依赖

- `board/` 文件夹包含所有必需的模块
- Python 3.x 或 PyPy3
- GUI需要: `pygame` 和 `pygame.freetype`

## C++版本

**位置**: `cpp/`

这是C++版本的最新实现，包含：
- AI3: 在AI2基础上做了细节调优
- AI4: 双递归AI（处理不确定子）
- AI5: 在AI3基础上增加了全局置换表

### 编译方法

```bash
cd cpp
mkdir build && cd build
cmake ..
make
```

### 配置

编辑 `players.conf` 来配置对局：
- 第一行：红方玩家（0=人类，1-5=AI）
- 第二行：黑方玩家
- 第三行：胜利阈值
- 第四行：对局日志路径

## 版本选择建议

- **学习/研究**: 使用Python版本，代码更易读
- **性能要求高**: 使用C++版本
- **继续开发**: 建议基于C++版本重构为Rust，因为：
  1. C++版本修复了Python版本的已知bug
  2. 代码结构更接近系统级语言
  3. 性能优化更完善

