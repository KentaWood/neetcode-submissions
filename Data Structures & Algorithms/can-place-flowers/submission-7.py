class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        able = 0
        
        for i,plot in enumerate(flowerbed):

            left_plot = flowerbed[i - 1] if i - 1 >= 0 else 0
            right_plot = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0

            # print(i,left_plot, plot ,right_plot)

            if left_plot == 0 and right_plot == 0 and  plot == 0:
                # print("here")
                able += 1
                flowerbed[i] = 1
            # print(flowerbed,able)
            
                
            
        return able >= n



    


        