class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c_map = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        length = len(digits)
        res = ['']
        all_results = []
        if length == 0:
            return []
        if length == 1:
            return c_map[digits]
        for each in digits:
            all_results.append(c_map[each])
        for answer in all_results:
            new_list = []
            for each in res:
                for piece in answer:
                    new_list.append(each+piece)
            res = new_list
        return res