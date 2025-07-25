package kyu8;

public class CalcAverage {
    public static double findAverage(int[] array) {
        double total = 0;
        int arrayLen = array.length;
        for (int i = 0; i < arrayLen; i++) {
            total += array[i];
        }
        return total / arrayLen;
    }
}
//https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/java
//You have passed all the tests! :)
