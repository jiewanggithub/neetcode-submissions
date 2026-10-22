class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_ = defaultdict(list)

        for s in strs:
            counter = Counter(s)
            key = tuple(sorted(list(counter.items())))
            list_[key].append(s)
        
        return list(list_.values())