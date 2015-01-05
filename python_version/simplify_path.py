"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):  # more practice
        st = []
        if path[0] != '/':
            return ''

        path = path.strip()
        path = path.strip('/')  # need to remove the leading and trailing '/'s, otherwise will yield additional ''s in path_list
        path_list = path.split('/')

        for i, token in enumerate(path_list):
            if token == '':   # if path == '/a///b'  additional / will yield a '' in the path_list
                continue
            elif token == '..':
                if len(st) > 0:
                    st.pop()
                else:
                    continue   # /a/../../.......'
            elif token == '.':
                continue
            else:
                st.append(token)

        res = ''
        for token in st:
            res += ('/' + token)

        if res == '':
            res = '/'

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath('/home/'))
    print(sol.simplifyPath('/a/./b/../../c/'))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath('/home//foo/'))
    print(sol.simplifyPath('/...'))
    print(sol.simplifyPath('/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///'))




