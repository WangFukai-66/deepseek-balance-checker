# deepseek-balance-checker
macOS tool: One‑click check DeepSeek API balance &amp; token estimate, with AppleScript shortcut.
```markdown

> macOS 一键查询 DeepSeek API 账户余额工具，搭配 AppleScript，快速估算可用 Token 数量。

✨ **功能特性**
- 分别查询赠送余额、充值余额、账户总可用余额
- 根据单价自动换算可调用百万 Token 数量
- 彩色终端面板输出，信息直观清晰
- 配套 AppleScript，macOS 支持一键唤起运行
- 使用 DeepSeek 官方开放接口

## 🚀快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/WangFukai-66/deepseek-balance-checker.git
cd deepseek‑balance‑checker
```

### 2. 配置 API Key
打开 `tokens.py`，修改配置区域填入你的密钥：
```python
API_KEY = "sk‑xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
密钥获取地址：[DeepSeek开放平台](https://platform.deepseek.com/api_keys)


### 3. 运行脚本
```bash
python3 tokens.py
```

## 🍎 macOS AppleScript 使用说明
1. 打开仓库内 `run‑shortcut.applescript`
2. **必须修改脚本中 python3 指向 tokens.py 的绝对路径，改为你本机文件位置**
3. 两种运行方式：
- 在「脚本编辑器」打开直接点击运行
- 导入 macOS 快捷指令，实现桌面一键唤起终端查看余额

## ⚠️重要说明
1. **价格估算限制**
`deepseek‑v4‑flash` 存在高峰/平峰分时计价，**没有设计接口爬取实时价格（以后可能会加），且没有接口可以获取当前处于哪个时段**。
输出的 Token 数值**仅作为估算参考，不作为计费依据，官方后台账单才是真实消耗**。

2. 接口说明
程序调用 DeepSeek 官方余额查询接口，请勿高频循环调用，避免触发平台限流。

3. 安全提醒
妥善保管以 `sk‑` 开头的密钥，密钥泄露会造成额度被盗刷。
