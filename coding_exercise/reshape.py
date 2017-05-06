class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # if matrix is reshapable:
            # return original matrix
        # else:
            # transform- flat- reshape
            # return matrix

        r_org=len(nums)
        c_org=len(nums[0])
        if r_org*c_org!=r*c:
            return nums
        else:
            nums_flat=[]
            for i in range(r_org):
                for j in range(c_org):
                    nums_flat.append(nums[i][j])
            print nums_flat
            nums_matrix=[[None]*c for x in range(r)]  # run into linage problem
            if r==1:
                for i, x in enumerate(nums_flat):
                    nums_matrix[0][i]=x
            else:
                x=0
                for i in range(len(nums_matrix)):
                    for j in range(len(nums_matrix[0])):
                            nums_matrix[i][j]=nums_flat[x]
                            x+=1
        return nums_matrix


x=Solution()
#print x.matrixReshape([[1,2,4],[3,4,2]],2,3)
#print x.matrixReshape([[1,2,3],[3,4,1]],3,2)
#print x.matrixReshape([[1,2],[3,4]],1,4)
print x.matrixReshape([[1,2],[3,4]],4,1)
print x.matrixReshape([[1,2,3],[4,5,6]],3,3)