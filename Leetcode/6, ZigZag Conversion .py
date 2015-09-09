class Solution(object):
    def convert(self, s, numRows):
        """
            :type s: str
            :type numRows: int
            :rtype: str
            """
        #the relationship between "PAYPALISHIRING" -> "PAHNAPLSIIGYIR".
        '''
            P   A   H   N
            A P L S I I G
            Y   I   R
            '''
        #3 rows -> we can build 3 array to collect the data, then combine them into one string
        #every 4 is a iteration, so the size of iteration = numRows *2 - 2
        '''
            A[0] = ['p', 'A', 'H', 'N']
            A[1] = ['A', 'p', 'L', 'S', 'I', 'I', 'G']
            A[2] = ['Y', 'I', 'R']
            '''
        #index = numRows -1 - abs(numRows - 1 - i % (2 * numRows - 2))
        
        #corner cases
        if len(s) <= numRows or numRows <= 1:
            return s
        
        #build a list of lists
        final = [[]for i in range(numRows)]
        
        for i in range(0, len(s)):
            final[numRows -1 - abs(numRows - 1 - i % (2 * numRows - 2))].append(s[i])
        
        #combine
        return ''.join([''.join(item) for item in final])