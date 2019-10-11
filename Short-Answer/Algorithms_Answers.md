#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

    O(n)

b)

    O(n*log(n)

c)

    O(n)

## Exercise II



    def break_height(building_height, f):   
    
        def throw(top, bottom, f):
            mid = ((top - bottom) / 2) + bottom #(round down)
            if floor == mid:
                return mid
            else if f > mid:
                return throw(top, mid, f)
            else if f < mid:
                return throw(mid, bottom, f)
        
        return throw(building_height, 0, f)
                
this is binary search, so time complexity should be log(n)
        