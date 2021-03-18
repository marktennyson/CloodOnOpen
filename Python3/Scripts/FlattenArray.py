class FlattenArray:
    def __init__(self) -> None:
        self.joinedArray:list = list()
    def flatter(self, Arr:list) -> list:
        for item in Arr:
            if isinstance(item, list): self.flatter(item)
            else: self.joinedArray.append(item)
        return self.joinedArray


def main() -> None:
    inp1:list = [1, [], [3, [[4]]]]
    inp2:list = [[["a"]], [["b"]]]
    inp3:list =[1, [2], [3, [[4]]]]
    inp4:list =[1, {}, [3, [[4]]]]
    inpL:list = [inp1, inp2, inp3, inp4]
    for inputs in inpL:
        fa:FlattenArray = FlattenArray()
        ansArray:list = fa.flatter(inputs)
        print (ansArray)

if __name__ == "__main__":
    main()

