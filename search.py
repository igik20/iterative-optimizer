import math

Class Midpoint_Search:

    def f(x):
        return 1 / x


    def midpoint_search(func, lower, upper, niter):
        mid = (upper + lower) / 2
        for i in range(niter):
            eps = (upper - lower) / 10

            m_plus = mid + eps
            m_minus = mid - eps

            f_plus = func(m_plus)
            f_minus = func(m_minus)

            if f_plus > f_minus:
                lower = mid
            else:
                upper = mid
            mid = (upper + lower) / 2

        return mid, func(mid)


    def main():
        print(midpoint_search(f, -2, 2, 50))

#I don't think we need this part as it's a class now.
#if __name__=="__main__":
    #main()
