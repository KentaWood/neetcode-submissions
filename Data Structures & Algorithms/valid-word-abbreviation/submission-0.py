class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        abbr_length = 0

        ap = 0
        wp = 0

        
        while ap < len(abbr) and wp < len(word):  

            print(word[wp], abbr[ap]) 
            
            # start of a abrreviation and check if the abrervsitoin is okay
            if abbr[ap].isdigit():
                print("here 1 ")

                # l eading zero 
                if abbr[ap] == "0":
                    return False

                i = 0

                while i + ap < len(abbr) and abbr[ap + i].isdigit():
                    i += 1 
                
                print(ap, i, abbr[ap:i])
                wp += int(abbr[ap: ap + i])
                ap += i


            # letter and check if the letter matches
            else:
                print("here")

                if word[wp] == abbr[ap]:
                    ap += 1 
                    wp += 1 

                else:
                    return False
        
        return wp == len(word)