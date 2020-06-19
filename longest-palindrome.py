

class Solution(object):

    def longestPalindrome(self, s):
        # if s is empty, return s
        if not s or len(s) <=1:
            return s

        # set longest to first letter of s
        longest = s[0:1]
        for (i,letter) in enumerate(s):
            # expand from center (where letter is center) by setting begin and end
            current = self.expand(s, i, i)
            # if current is longer than longest, overwrite longest
            if len(current) > len(longest):
                longest = current
            # need to repeat since there could be two centers
            current = self.expand(s, i, i+1)
            if len(current) > len(longest):
                longest = current
        print(longest)
        return longest

    def possible_palindrome(self, s, begin, end):
        return s[begin] == s[end]

    def has_hit_bounds(self, s, begin, end):
        return begin >= 0 and end <= len(s) - 1

    def expand(self, s, begin, end):
        # if first and last letter match, expand outwards on both sides until
        # hitting boundaries on either side
        while(self.has_hit_bounds(s, begin, end)
                and self.possible_palindrome(s, begin, end)):
            begin -= 1
            end += 1
        return s[begin+1:end]

Solution().longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy")
