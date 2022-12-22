/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func dfs(curr *TreeNode) int{
    if curr==nil{
            return 0
        
    }
        var a int= dfs(curr.Left)
        var b int= dfs(curr.Right)
    return int(math.Max(float64(a),float64(b))) +1
        
    }
func maxDepth(root *TreeNode) int {
    var a int= dfs(root)
    return a
}