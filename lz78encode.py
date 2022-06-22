import typing
import argparse


class Lz78Code:
    def __init__(self, i: int, c: str):
        self.i = i
        self.c = c

    def __str__(self) -> str:
        return f"<{self.i}, '{self.c}'>"


def encode(input_str: str) -> typing.List[Lz78Code]:
    ret = []
    sub = ""
    sub_dict = [""]
    for c in input_str:
        it = sub_dict.count(sub + c)
        if it == 0:
            it2 = sub_dict.index(sub)
            code = Lz78Code(it2, c)
            ret.append(code)
            sub_dict.append(sub + c)
            print(f"'{sub_dict[-1]}'\t{str(code)}\t{len(sub_dict)-1}")
            sub = ""
        else:
            sub += c
    return ret


def decode(input_ar: typing.List[Lz78Code]) -> str:
    ret = ""
    sub_dict = [""]
    for code in input_ar:
        sub = sub_dict[code.i] + code.c
        sub_dict.append(sub)
        ret += sub
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_str",
        type=str,
    )
    args = parser.parse_args()

    ret = encode(args.input_str)
    print(f"{len(ret)=}")
    print(*ret)
    print(f"decoded: '{decode(ret)}'")
