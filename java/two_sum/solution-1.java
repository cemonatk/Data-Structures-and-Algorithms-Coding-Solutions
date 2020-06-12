import java.util.*;

class Code {
  public static int[] twosum(int[] array, int sum) {
		int result[] = new int[2];
		
		for (int num1: array){
			for (int num2: array){
				if (num1 + num2 == sum && num1 != num2)
				{
					result[0] = num1;
					result[1] = num2;
				}
			}
		}
		if (result[0] == 0 && result[1] == 0){
			return new int[]{};
		}
    return result;
  }
}

