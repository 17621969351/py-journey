import sys


def greet(name: str, city: str) -> str:
    return f"你好呀, {name}! 你来自{city},今天是学习Python的第一天。"


def main() -> None:
    args = sys.argv[1:]
    if len(args) < 2:
        print("用法: python3.12    hello.py <名字> <城市>")
        sys.exit(1)
    print(greet(args[0], args[1]))


if __name__ == "__main__":
    main()
