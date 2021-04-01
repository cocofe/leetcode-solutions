
# @Title: TinyURL 的加密与解密 (Encode and Decode TinyURL)
# @Author: cocofe
# @Date: 2020-02-11 00:22:49
# @Runtime: 20 ms
# @Memory: N/A

class Codec:
    
    hash_url_map = {}
    url_hash_map = {}
    prefix = 'http://tinyurl.com/'
    
    def hash(self, url):
        if url in self.url_hash_map:
            return self.url_hash_map[url]
        length = len(self.hash_url_map)
        code = hex(length+1)
        code = code[2:]
        if len(code) < 6:
            code = '0' * (6 - len(code)) + code
        self.hash_url_map[code] = url
        self.url_hash_map[url] = code
        return code

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        return self.prefix + self.hash(longUrl)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl.split(self.prefix)[-1]
        return self.hash_url_map.get(code)  
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
