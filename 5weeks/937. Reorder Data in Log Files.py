class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        d, l = [], []

        for log in logs:
            if log.split()[1].isdigit():
                d.append(log)
            else:
                l.append(log)
        
        l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return l + d
