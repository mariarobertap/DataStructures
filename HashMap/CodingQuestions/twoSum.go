func twoSum(nums []int, target int) []int {
    
    
    
    m := make(map[int]int)
    var res = []int{0, 0}

    
    for i:= 0; i <= len(nums); i++{
        key := target - nums[i]
        
        if value, ok := m[key]; ok {
             res[0], res[1] = i, value
            return  res
        }else{
            m[nums[i]] = i
            
        }
    }
    
    return res
    
}
