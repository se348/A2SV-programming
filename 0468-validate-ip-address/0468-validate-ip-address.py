class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        forIPV4 = queryIP.split(".")
        
        
        NEITHER = "Neither"
        
        if (len(forIPV4 ) != 1):
            if len(forIPV4) != 4:
                return NEITHER
            for charachter in forIPV4:
                if not charachter or not(charachter.isnumeric()):
                    return NEITHER
                if not (0 <= int(charachter) <= 255) or str(int(charachter)) != charachter:
                    return NEITHER
            return "IPv4"
        
        ipv6 = queryIP.split(":")
        
        if len(ipv6) != 8:
            return NEITHER
        
        for part in ipv6:
            if not (1 <= len(part) <= 4):
                return NEITHER
            
            for charachter in part:
                if not("0" <= charachter <= "9") and not("A" <= charachter <= "F") and not("a" <= charachter <= "f"):
                    return NEITHER
        return "IPv6"
            