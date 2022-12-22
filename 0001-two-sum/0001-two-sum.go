func twoSum(nums []int, target int) []int {
    var count []int
    for i := 0; i < len(nums); i++{
        for j:=i+1; j< len(nums); j++{
            if nums[i] + nums[j]==target{
                count =append(count,i)
                count =append(count,j)
                return count
            }
        }
    }
    return count
}