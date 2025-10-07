import numpy as np

# slicing
arr=np.arange(11)
print(arr)
print('slicing:',arr[2:7])
print('with step:',arr[1:8:2])
print('neagtive indexing:',arr[-3])

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('entire row',arr_2d[1])
print('entire col:',arr_2d[:,1])

# sorting
unsorted=np.array([3,4,1,1,5,9,6])
print('sorted:',np.sort(unsorted))
arr_2dus=np.array([[3,1],[1,2],[2,3]])
print("sorted by row:",np.sort(arr_2dus,axis=1))
print("sorted by col:",np.sort(arr_2dus,axis=0))

#filter
num=np.array([1,2,3,4,5,6,7,8,9])
even_num=num[num%2==0]
print("even num:",even_num)

#filter with mask
mask=num>5
print("mask:",mask)
print("num>5:",num[mask])

#fancy indexing vs np.where()
indicies=[0,2,4]
print("indices:",num[indicies])
where_result=np.where(num>5)
print("where:",where_result)
print(num[where_result])

cond_array=np.where(num>5)
print("cond_array:",cond_array)
# np.where(num>5,"ture","false")
# if(num>5){
#     'true'
# }else{
#     "false"
# }

#add and removeing data
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
comb=arr1+arr2
print("comb:",comb)
concat=np.concatenate((arr1,arr2))
print("concat:",concat)

#array compatibility
a=np.array([1,2,3])
b=np.array([4,5,6,7])
c=np.array([7,8,9])
print('compatibility:',a.shape==b.shape)
print('compatibility:',a.shape==c.shape)

og=np.array([[1,2],[3,4]])
new_row=np.array([[5,6]])
with_new_row=np.vstack(og,new_row)
new_col=np.array([[7],[8]])
with_new_col=np.hstack(og,new_col)

# np.deleted(array)??