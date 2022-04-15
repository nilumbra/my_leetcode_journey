/**
 * Definition for node.
 * class Node {
 *     val: number
 *     children: Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function preorder(root: Node | null): number[] {
    const ans: number[] = [];
    
    function recurse(root: Node | null): void {
        if (root) {
            ans.push(root.val)
            for (const child of root.children) {
                recurse(child)
            }
        }
    }

    recurse(root)
    // console.log(ans)

    return ans
};