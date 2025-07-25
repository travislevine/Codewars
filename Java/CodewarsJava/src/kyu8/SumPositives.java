package kyu8;

public class SumPositives {
    public static int sum(int[] arr){
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0) {
                total += arr[i];
            }
        }
        return total;
    }

    public static void main(String[] args) {
        System.out.println(sum(new int[]{1, -4, 7, 12}));
    }
}
//https://www.codewars.com/kata/5715eaedb436cf5606000381/train/java
//You have passed all of the tests! :)
