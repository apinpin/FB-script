import java.util.HashMap;

public class MF {
    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        // mostFrequent(array1) should return 1.
        int[] array1 = {1, 3, 1, 3, 2, 1};
        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};

        System.out.println(mostFreqent(array3));
    }

    // Implement your solution below.
    public static Integer mostFreqent(int[] givenArray) {
        Integer maxItem = null;
        int arr_len = givenArray.length;
        if(arr_len == 0)
        {
            maxItem = null;
        }
        else if(arr_len == 1)
        {
            maxItem = givenArray[0]
        }
        else
        {
            HashMap hm = new HashMap();
            int key = givenArray[0];
            for(int i = 0; i < arr_len; i++)
            {
                if(!hm.containsKey(i))
                {
                    hm.put(i, 1);
                }
                else
                {
                    int temp = hm.get(i);
                    hm.replace(i, temp + 1);
                }
                
                if(hm.get(key) < hm.get(i))
                {
                    key = i;
                }
            }
            maxItem = key;
        }
        return maxItem;
    }
}

