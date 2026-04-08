class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ["JFK"]
        tickets.sort()
        ticket_map = {src:[] for src, dest in tickets}
        for s, d in tickets:
            ticket_map[s].append(d)
        tic_len = len(tickets)
        def dfs(src):
            if len(res) == tic_len + 1:
                return True
            if src not in ticket_map:
                return False
            tmp = ticket_map[src]
            for ind, ver in enumerate(tmp):
                res.append(ver)
                ticket_map[src].pop(ind)
                if dfs(ver):
                    return True
                res.pop()
                ticket_map[src].insert(ind, ver)
            return False
        dfs("JFK")
        return res