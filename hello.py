import sys


def greet(name: str) -> str:
    return f"Hello, {name}! 今天是学习Python的第一天。"


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("用法: python 3.12    hello.py <名字>")
        sys.exit(1)
    print(greet(args[0]))


if __name__ == "__main__":
    main()
