# https://hbj0209.tistory.com/97
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        answer = []
        IPs = []
        def valid(string):
            if len(string) == 1:
                return True
            if int(string) > 255 or string[0] == '0':
                return False
            return True
        
        def BT(index, ip):
            # 종료 조건
            if len(ip) > 4:
                return
            elif index == len(s) and len(ip) == 4:
                res = '.'.join(ip)
                answer.append(res)
                return
            
            idx = index + 3
            for i in range(index, min(len(s), idx)):
                num_str = s[index: i + 1]
                # 유효성 검사
                if valid(num_str):
                    IPs.append(num_str)
                    # 재귀 호출
                    print(IPs)
                    BT(index + len(num_str), IPs)
                    IPs.pop()
        
        ip = []
        BT(0, ip)
        return answer
