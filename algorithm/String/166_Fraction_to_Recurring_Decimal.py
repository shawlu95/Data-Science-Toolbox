class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        str_builder = []
        if numerator * denominator < 0:
            str_builder.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        str_builder.append(str(numerator // denominator))
        rem = numerator % denominator

        if rem == 0:
            return "".join(str_builder)

        str_builder.append(".")
        pos = {}
        while rem != 0:
            if rem in pos:
                str_builder.insert(pos[rem], "(")
                str_builder.append(")")
                break
            pos[rem] = len(str_builder)
            rem *= 10
            str_builder.append(str(rem // denominator))
            rem %= denominator
        return "".join(str_builder)
