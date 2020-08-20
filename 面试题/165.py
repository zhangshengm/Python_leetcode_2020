class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        #位数少的补零
        if len(v1)>len(v2):
           v2+=['0']*(len(v1)-len(v2))
        if len(v1)<len(v2):
           v1+=['0']*(len(v2)-len(v1))
        for i in range(len(v1)):
            if int(v1[i])==int(v2[i]):
                continue
            elif int(v1[i])>int(v2[i]):
                return 1
            else:
                return -1
        return 0
