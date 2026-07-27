class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r=0,mountainArr.length()-1
        full=r
        def search(l,r):
            
            if l>r:
                return -1
            m=(l+r)//2
            print(l,r,m)
            mtn = mountainArr.get(m)
            if target==mtn:
                return m
            mleft,mright =mountainArr.get(m-1),mountainArr.get(m+1)
            inc=True
            if mright<mtn:
                inc=False
            if not inc and mleft<mtn:
                lside=search(l,m-1)
                
                if lside!=-1:
                    return lside
                rside=search(m+1,r)
                if rside!=-1:
                    return rside
                else:
                    return -1
            if target<mtn:
                if inc:
                    return search(l,m-1)
                else:
                    return search(m+1,r)
            else:
                if inc:
                    return search(m+1,r)
                else:
                    return search(l,m-1)
        return search(l,r)


                
                
