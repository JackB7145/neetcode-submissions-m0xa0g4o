class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        each child is assigned a rating, 

        a children with different ratings should get less candies than their

        adjacent child with a lower rating

        This screams dp
        
        the minimum number of candies an ith child can get

        is dependant on the minimum number of candies its left and right adjacent

        member gets

        perhaps create a dp of length rating which all  have 1

        sort the original on into pairs of indexes and ratings

        start at the least and don't change them that equal that first one, so snip the tip

        then go layer by layer

        
        '''

        dp = [1 for _ in range(len(ratings))]
        ratingsOrder = ([(v, i) for i, v in enumerate(ratings)])
        ratingsOrder.sort()

        ratings = [(v, i) for i, v in enumerate(ratings)]

        for value, idx in ratingsOrder:
            leftChild = ratings[idx-1] if idx > 0 else (float('inf'), idx)
            rightChild = ratings[idx+1] if idx < len(ratings)-1 else (float('inf'), idx)

            count = 1

            if leftChild[0] < value:
                count = max(count, dp[leftChild[1]] + 1)
            
            if rightChild[0] < value:
                count = max(count, dp[rightChild[1]] + 1)

            dp[idx] = count
            print(f'Evaluating at {value} we have states {dp}')


        return sum(dp)


            

        