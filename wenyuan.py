import requests
import time

URL = "http://10.10.16.12/api/portal/v1/login"

DATA = {
    "domain": "telecom",
    "username": "17315559717",
    "password": "246135"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Origin": "http://10.10.16.12",
    "Referer": "http://10.10.16.12/portal/"
}


def login():
    try:
        r = requests.post(URL, json=DATA, headers=HEADERS, timeout=5)

        print("状态码:", r.status_code)

        try:
            print("返回JSON:", r.json())
        except:
            print("返回文本:", r.text)

        if r.status_code == 200:
            print("✅ 登录请求发送成功（已强制刷新连接）")
        else:
            print("❌ 登录失败")

    except Exception as e:
        print("❌ 请求异常:", e)


def is_online():
    try:
        requests.get("https://www.baidu.com", timeout=3)
        return True
    except:
        return False


def run():
    print("======== 自动联网任务 ========")

    if not is_online():
        print("⚠️ 当前断网 → 正在登录")
        login()
    else:
        print("✅ 已在线 → 执行强制重连（防掉线）")
        login()

    print("================================\n")


if __name__ == "__main__":
    run()