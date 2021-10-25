from typing import Any


def form07(x: Any, y: Any, z: Any):
    print("{}時の{}は{}".format(x, y, z))

def main():
    x=12
    y="気温"
    z=22.4
    form07(x, y, z)

if __name__ == "__main__":
    main()