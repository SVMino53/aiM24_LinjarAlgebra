class Frac:
    """
    A mathematical fraction.

    Attributes:
        num(int):
            Numerator
        den(int):
            Denominator
    """
    def __init__(self, num : int, den : int) -> None:
        """
        Args:
            num(int):
                Numerator
            den(int):
                Denominator
        """
        self.num = num
        self.den = den
        self.__simplify()

    @property
    def num(self) -> int:
        """
        Numerator
        """
        return self.__num
    
    @num.setter
    def num(self, val : int) -> None:
        if not isinstance(val, int):
            raise TypeError(f"'num' is of type {type(val).__name__}; must be 'int'")
        self.__num = val

    @property
    def den(self) -> int:
        """
        Denominator
        """
        return self.__den
    
    @den.setter
    def den(self, val : int) -> None:
        """
        Denominator
        """
        if not isinstance(val, int):
            raise TypeError(f"'den' is of type {type(val).__name__}; must be 'int'")
        if val <= 0:
            raise ValueError(f"'den' value is {val}; must be > 0")
        self.__den = val

    # Private
    def __simplify(self) -> None:
        divid = max(abs(self.num), self.den)
        divis = min(abs(self.num), self.den)
        rest = divid % divis
        while rest != 1:
            if rest == 0:
                self.num //= divis
                self.den //= divis
                break
            divid = divis
            divis = rest
            rest = divid % divis

    # Representation
    def __repr__(self) -> str:
        return f"Frac(num={self.num}, den={self.den})"
    
    def __str__(self) -> str:
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"
    
    # Compare
    def __eq__(self, other : "Frac") -> bool:
        return self.num == other.num and self.den == other.den
    
    # Calculate
    def __add__(self, other : "Frac") -> "Frac":
        return Frac(self.num*other.den + other.num*self)
    

a = Frac(2, 3)
b = Frac(14, 4)

print(a, b)
print(a == a)
print(a == b)