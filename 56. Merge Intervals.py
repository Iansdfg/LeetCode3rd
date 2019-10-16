class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        merge = []
        for i in range(len(intervals)):
            if merge == []:
                merge.append(intervals[i])
            else:
                if intervals[i][0]<=merge[-1][1]:
                    merge[-1][:] = [merge[-1][0]]+[max(merge[-1][1], intervals[i][1])]
                else:
                    merge.append(intervals[i])
        return merge
