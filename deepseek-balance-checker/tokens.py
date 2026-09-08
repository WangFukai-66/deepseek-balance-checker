import requests

# ===================== 替换成你的sk密钥 =====================
API_KEY = "sk‑xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# V4-Flash 平峰价格 0.2元/百万输入token（若改价可自行配置）
PRICE_PER_MILLION_INPUT = 0.20
# ==================================================================

# V4-Flash 平峰价格 0.2元/百万输入token
PRICE_PER_MILLION_INPUT = 0.20
MODEL_NAME = "deepseek-v4-flash"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def format_money(num: float) -> str:
    return f"¥{num:.2f}"

def money_to_tokens(money: float) -> str:
    if money <= 0:
        return "0"
    million_tokens = money / PRICE_PER_MILLION_INPUT
    return f"{million_tokens:.2f} 百万 Tokens"

try:
    resp = requests.get("https://api.deepseek.com/user/balance", headers=headers, timeout=10)
    data = resp.json()

    if resp.status_code != 200:
        print(f"\033[31m❌ 请求失败 状态码：{resp.status_code}\033[0m")
        print(f"原始返回数据：{data}")
    else:
        # 提取人民币CNY余额数据
        cny_data = None
        for info in data["balance_infos"]:
            if info["currency"] == "CNY":
                cny_data = info
                break

        if not cny_data:
            print("\033[31m❌ 未找到人民币余额信息\033[0m")
        else:
            # 字符串转浮点数
            granted = float(cny_data["granted_balance"])
            topped = float(cny_data["topped_up_balance"])
            total = float(cny_data["total_balance"])
            usable = data["is_available"]

            print("\033[36m====================================================\033[0m")
            print("\033[1;34m           DeepSeek API 账户额度查询面板            \033[0m")
            print("\033[1;34m   DeepSeek开放平台：https://platform.deepseek.com    \033[0m")
            print("\033[36m====================================================\033[0m")
            print(f"\033[92m✅ 免费赠送余额：{format_money(granted)}")
            print(f"   可调用 {MODEL_NAME}：{money_to_tokens(granted)}\033[0m")
            print("-" * 50)
            print(f"\033[93m💰 充值现金余额：{format_money(topped)}")
            print(f"   可调用 {MODEL_NAME}：{money_to_tokens(topped)}\033[0m")
            print("-" * 50)
            print(f"\033[1;35m📊 账户总可用额度：{format_money(total)}")
            print(f"   合计可调用 {MODEL_NAME}：{money_to_tokens(total)}\033[0m")
            print("-" * 50)
            status = "\033[92m正常可用\033[0m" if usable else "\033[31m额度不足/不可用\033[0m"
            print(f"\033[94m📡 账户调用状态：{status}")
            print("\033[36m====================================================\033[0m")
            print("\033[90m💡 扣费顺序：优先消耗免费赠送额度，用完再扣充值余额")
            print(f"📌 计价参考：{MODEL_NAME} 平峰 {PRICE_PER_MILLION_INPUT}元/百万输入Token\033[0m")
            print("\033[36m====================================================\033[0m")

except requests.exceptions.Timeout:
    print("\033[31m❌ 请求超时，请关闭代理/VPN后重试\033[0m")
except requests.exceptions.ConnectionError:
    print("\033[31m❌ 网络连接失败，无法访问DeepSeek接口\033[0m")
except KeyError as e:
    print(f"\033[31m❌ 字段缺失错误：{e}")
    print("完整接口返回内容：")
    print(data)
except Exception as e:
    print(f"\033[31m❌ 程序异常：{str(e)}\033[0m")
