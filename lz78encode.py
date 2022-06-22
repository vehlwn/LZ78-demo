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
    prev_sub = ""
    sub_dict = {"": 0}
    for c in input_str:
        next_sub = prev_sub + c
        if next_sub not in sub_dict:
            i = sub_dict[prev_sub]
            code = Lz78Code(i, c)
            ret.append(code)
            sub_dict[next_sub] = len(sub_dict)
            print(f"'{next_sub}'\t{str(code)}\t{len(sub_dict)-1}")
            prev_sub = ""
        else:
            prev_sub = next_sub
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
