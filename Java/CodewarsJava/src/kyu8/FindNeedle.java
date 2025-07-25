package kyu8;

public class FindNeedle {
    public static String findNeedle(Object[] haystack) {
        for (int i = 0; i < haystack.length; i++) {
            if ("needle".equals(haystack[i])) {
                return "found the needle at position " + i;
            }
    }
        return "";
    }
}
//https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/java
//You have passed all of the tests! :)