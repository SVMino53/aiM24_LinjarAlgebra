from typing import Self, Literal
import re

class Frac:
    """
    A mathematical fraction.

    Attributes:
        num(int):
            Numerator of fraction.
        den(int):
            Denominator of fraction.
    """
    def __init__(self, val : Self | int | float | str, /, den : int = 1) -> None:
        """
        Args:
            val(int):
                Value to convert to `Frac` **or** numerator of fraction.
            den(int):
                **If val is an `int`:** Denominator of fraction. 
        """
        if not isinstance(val, (Frac, int, float, str)):
            raise TypeError()
        if not isinstance(den, int):
            raise TypeError()
        if isinstance(val, (Frac, float, str)) and den != 1:
            raise ValueError()
        if den == 0:
            raise ValueError()

        if isinstance(val, int):
            self.num = val
            self.den = den
            self._simplify()
        elif isinstance(val, Frac):
            self.num = val.num
            self.den = val.den
        elif isinstance(val, float):
            fr = self._float2frac(val)
            self.num = fr.num
            self.den = fr.den
        elif isinstance(val, str):
            fr = self._str2frac(val)
            self.num = fr.num
            self.den = fr.den

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
        if val == 0:
            raise ValueError(f"'den' value is {val}; must not be 0")
        self.__den = val

    # Private
    def _simplify(self) -> None:
        if self.num == 0:
            self.den = 1
            return
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

    def _float2frac(self, val : float) -> Self:
        pass

    def _str2frac(self, val: str) -> Self:
        if not isinstance(val, str):
            raise TypeError()
        if not re.match(r"^-?\d*(\/\d*)?$", val):
            raise ValueError()
        
        if "/" in val:
            num, den = val.split("/")
            num = int(num)
            den = int(den)
        else:
            num = int(val)
            den = 1
        return Frac(num, den)

    # Representation
    def __repr__(self) -> str:
        return f"Frac(num={self.num}, den={self.den})"
    
    # Type conversion
    def __str__(self) -> str:
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"
    
    def __float__(self) -> float:
        return self.num/self.den
    
    def __int__(self) -> int:
        if self.den == 1:
            return self.num
        else:
            return int(float(self))
    
    def __bool__(self) -> bool:
        return bool(self.num)
    
    # Compare
    def __eq__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, Frac):
            return self.num == other.num and self.den == other.den
        elif isinstance(other, int):
            return self.num == other and self.den == 1
        elif isinstance(other, float):
            return float(self) == other
    
    def __ne__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, Frac):
            return self.num != other.num or self.den != other.den
        elif isinstance(other, int):
            return self.num != other or self.den != 1
        elif isinstance(other, float):
            return float(self) != other
    
    def __lt__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        return float(self) < float(other)
    
    def __le__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        return float(self) <= float(other)
    
    def __gt__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        return float(self) > float(other)
    
    def __ge__(self, other : Self | int | float) -> bool:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        return float(self) >= float(other)
    
    # Operations
    def __add__(self, other : Self | int | float) -> Self:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.num*other.den + other.num*self.den, self.den*other.den)
    
    def __sub__(self, other : Self | int | float) -> Self:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.num*other.den - other.num*self.den, self.den*other.den)
    
    def __neg__(self) -> Self:
        return Frac(-self.num, self.den)
    
    def __mul__(self, other : Self | int | float) -> Self:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.num*other.num, self.den*other.den)

    def __truediv__(self, other : Self | int | float) -> Self:
        if not isinstance(other, (Frac, int, float)):
            raise TypeError()
        
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.num*other.den, self.den*other.num)
    
    def __pow__(self, other : int | Self | float) -> Self | float:
        if not isinstance(other, (int, Self, float)):
            raise TypeError()
        
        if isinstance(other, int):
            return Frac(self.num**other, self.den**other)
        else:
            return float(self)**float(other)
        
class GaussMatrix:
    def __init__(self, content : list[list[Frac, int, float]] | None = None) -> None:
        if content is None:
            self.content = [[Frac(0)]*4, [Frac(0)]*4, [Frac(0)]*4]
        else:
            self.content = [[Frac(val) for val in row] for row in content]

    # Representation
    def __repr__(self) -> str:
        pass

    # Type conversion
    def __str__(self) -> str:
        text = ""
        widths = [len(str(val)) for val in self.content[0]]
        for row in self.content[1:]:
            widths = [max(widths[i], len(str(val))) for i, val in enumerate(row)]
        for row in self.content:
            text += "|"
            for i, val in enumerate(row[:-1]):
                text += f" {str(val):{widths[i]}} "
            text += f"| {str(row[-1]):{widths[-1]}} |\n"
        return text

    def as_equations(self) -> str:
        pass

    def to_list(self) -> list[list[Frac]]:
        return self.content

    # Other methods
    def fill_in(self) -> None:
        pass

    def row_swap(self, row_x_ind : int, row_y_ind : int) -> None:
        temp = self.content[row_x_ind]
        self.content[row_x_ind] = self.content[row_y_ind]
        self.content[row_y_ind] = temp

    def row_addition(self, row_from_index : int, row_to_index : int, multiplyer : Frac = Frac(1)) -> None:
        for i in range(len(self.content[row_from_index])):
            self.content[row_to_index][i] += self.content[row_from_index][i] * multiplyer

    def row_multiplication(self, row_index : int, multiplyer : Frac) -> None:
        for i in range(len(self.content[row_index])):
            self.content[row_index][i] *= multiplyer

    def solve(self, stepwise : bool = False, inplace : bool = False) -> Self | None:
        for i in range(len(self.content[0]) - 1):
            for j in range(i, len(self.content)):
                if self.content[j][i] != 0:
                    if i != j:
                        print(f"Row_{i + 1} <-> Row_{j + 1}")
                        print()
                        self.row_swap(i, j)
                        print(self)
                    if self.content[i][i] != 1:
                        mul = Frac(1)/self.content[i][i]
                        print(f"Row_{i + 1} = {mul} * Row_{i + 1}")
                        print()
                        self.row_multiplication(i, mul)
                        print(self)
                    for k in range(i + 1, len(self.content)):
                        if self.content[k][i] != 0:
                            mul = -self.content[k][i]
                            if mul < 0:
                                print(f"Row_{k + 1} = Row_{k + 1} - {-mul} * Row_{i + 1}")
                            else:
                                print(f"Row_{k + 1} = Row_{k + 1} + {mul} * Row_{i + 1}")
                            print()
                            self.row_addition(i, k, mul)
                            print(self)
                    break
        for i in range(len(self.content) - 1, 0, -1):
            if self.content[i][:-1].count(Frac(0)) == len(self.content[0]) - 1:
                if self.content[i][-1] != 0:
                    print(f"Contradiction on row {i + 1}! There are no solutions!")
                    return
            else:
                for j in range(0, i):
                    if self.content[j][i] != 0:
                        mul = -self.content[j][i]
                        if mul < 0:
                            print(f"Row_{j + 1} = Row_{j + 1} - {-mul} * Row_{i + 1}")
                        else:
                            print(f"Row_{j + 1} = Row_{j + 1} + {mul} * Row_{i + 1}")
                        print()
                        self.row_addition(i, j, mul)
                        print(self)
        ans = [""]*(len(self.content[0]) - 1)
        par_ind = 1
        for i in range(len(self.content[0]) - 2, -1, -1):
            if i >= len(self.content) or self.content[i][i] == 0:
                ans[i] = f"t_{par_ind}"
                par_ind += 1
            else:
                ans[i] = f"{self.content[i][-1]}"
                for j in range(i + 1, len(ans)):
                    c = self.content[i][j]
                    if c < 0:
                        ans[i] += f" + {-c}*{ans[j]}"
                    elif c > 0:
                        ans[i] += f" - {c}*{ans[j]}"
        ans_str = f"({ans[0]}"
        for i in range(1, len(ans)):
            ans_str += f", {ans[i]}"
        ans_str += ")"
        if par_ind > 1:
            ans_str += "  t_1"
            for i in range(2, par_ind):
                ans_str += f", t_{i}"
            ans_str += " \u2208 \u211d"
        print(f"Answer: {ans_str}")