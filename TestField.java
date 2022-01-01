import java.util.HashSet;
import solutions.solutions.NextPermutation;
public class TestField {
    public static void main(String args[]){
        // TestField tf = new TestField();
        // tf.testNextPermutation31();

        
    }

    // 31 Next Permutation
    private void testNextPermutation31(){
        NextPermutation np = new NextPermutation();
        // int[] nums = {5, 4, 3, 2, 1}; 
        int[] nums = {1, 5, 4, 3, 2};
        np.Next(nums); // Expecting 14532
    }
}