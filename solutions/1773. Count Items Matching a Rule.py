class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            count=0
            for i in range(len(items)):
                if items[i][0]== ruleValue:
                    count+=1
            return count
        if ruleKey == "color":
            count=0
            for i in range(len(items)):
                if items[i][1]== ruleValue:
                    count+=1
            return count
        if ruleKey == "name":
            count=0
            for i in range(len(items)):
                if items[i][2]== ruleValue:
                    count+=1
            return count
        
