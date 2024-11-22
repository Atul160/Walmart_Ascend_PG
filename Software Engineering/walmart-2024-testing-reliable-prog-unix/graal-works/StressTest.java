package com.naveen;

public class StressTest {
    public static void main(String[] args) {

        long startTime = System.nanoTime();

        long counter = 0;
        final int LIMIT = 1_000_000;

        for (int i = 0; i < LIMIT; i++) {
            for (int j = 0; j < LIMIT; j++) {
                counter++;
            }
        }

        long endTime = System.nanoTime();
        System.out.println("Total Tim For iteration is :" + (endTime - startTime));

    }
}
