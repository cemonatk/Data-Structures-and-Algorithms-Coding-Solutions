import java.util.*;

class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
    Map<Integer, Boolean> numbers = new HashMap<>();
    
    //foreach
    for(int num : array){
    int pair = targetSum - num;

    if (numbers.containsKey(pair)){
        return new int[] {pair, num};
    } else {
        numbers.put(num, true);
    }
    }
    return new int[0];		
  }
}