class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #. phone #.   gender   age      seat alloted?
        # "7868190130   M       75      22"

        # print(details[0][11:13])

        ans = 0

        for person in details:

            ans += 1 if int(person[11:13]) > 60 else 0

        return ans