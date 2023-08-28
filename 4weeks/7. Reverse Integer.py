class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        str_x = str(abs(x))
        str_x_reversed = str_x[::-1]
        result = int(str_x_reversed)
        result = result * -1 if x < 0 else result

        return result if (result < max_int and result > min_int) else 0
