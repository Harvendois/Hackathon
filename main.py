class A:
    def __init__(
        self,
    ) -> None:
        print("A.__init__")

    def fib(
        self,
        x: int,
        y: int,
    ) -> int:
        if x <= 1:
            return x
        return self.fib(y, x + y)

    def foo(
        self,
        x: float,
    ) -> list[str]:
        return [str(x)]

    def bar(
        self,
    ) -> tuple[str, str]:
        return ("a", "b")
