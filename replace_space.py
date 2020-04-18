class Solution():
    def replace_space(self, string):
        return string.replace(' ', "%20")


if __name__ == "__main__":
    s = Solution()
    string01 = 'We are happy'
    ans = s.replace_space(string01)
    print(ans)