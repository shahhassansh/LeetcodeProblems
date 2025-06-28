# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        baseURL = 'http://'+startUrl.split('//')[1].split('/')[0]
        out = set()
        q = set()
        q.add(startUrl)
        while q:
            t = q.pop()
            out.add(t)
            child_urls = htmlParser.getUrls(t)

            for a in child_urls:
                if a not in out:
                    if a not in q:
                        if a.startswith(baseURL):
                            q.add(a)
        return list(out)

        
