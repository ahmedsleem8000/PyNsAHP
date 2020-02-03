from ivns.ivns import Ivns
import copy


class norm:

    def linear(self, x, xmax, beneficial):
        result = xmax.Division(x, xmax)
        if isinstance(result, int) and result == 0:
            return 0
        else:
            if beneficial:
                return result
            else:

                return result.onediff(result)

    def linearMaxMin(self, x, xmax, xmin, beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        MaxMinDiff = ivns.Difference(xmax, xmin)
        if beneficial:
            overPart = ivns.Difference(x, xmin)
        else:
            overPart = ivns.Difference(xmax, x)

        return ivns.Division(overPart, MaxMinDiff)

    def linearSum(self, x, xmax, xmin, beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        MaxMinDiff = ivns.Difference(xmax, xmin)
        if beneficial:
            overPart = ivns.Difference(x, xmin)
        else:
            overPart = ivns.Difference(xmax, x)

        return ivns.Division(overPart, MaxMinDiff)
