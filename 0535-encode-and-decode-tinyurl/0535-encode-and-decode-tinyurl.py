class Codec:
    def __init__(self):
        self.map = {}
        self.shortUrlMap = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        curr_str = ""

        for i in range(8):    
            j = randint(48, 122)
            curr_str += chr(j)
        
        if curr_str in self.map:
            return self.encode(longUrl)
        
        self.shortUrlMap[curr_str] = longUrl 
        self.map[longUrl] = curr_str
        
        return self.map[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.shortUrlMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))