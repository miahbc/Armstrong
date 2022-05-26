import functools

# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):

    arm_nums = []
    sum = 0
    # print(numbers)

    for x in numbers:
        # print(x)
        sum = []
        x= str(x)
        # print(x)
        # print(str(xx))
        for y in x:
            sum.append(int(y)**len(x))
        # print(sum)
        sum2 = functools.reduce(lambda agg, item: agg + item, sum)
        # print(sum2)
        if sum2 == int(x):
            arm_nums.append(sum2)
    return arm_nums


        
    


# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])


# JAVASCRIPT VERSION BELOW:
# // How can you make this more scalable and reusable later?

# exports.findArmstrongNumbers = function (n) {

# let armNums = []
# let sum = 0
# for (let i=0; i<n.length; i++) {
#     // console.log(n[i].toString().split(''))
#     let arr = n[i].toString().split('')
#     for (let j=0; j<arr.length; j++) {
#         sum += (arr[j]**(arr.length))
#         // console.log(sum)
#         if (sum === n[i]) {
#             if (!armNums.includes(sum)) {
#                 armNums.push(sum)
#             }   
#         }
#     } sum = 0
# } 

#  return armNums
# } 


