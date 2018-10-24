package org.test;

import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public final class App {

    public static String guessNumber() throws IOException {

        int a = 1000000;
        int b = 1;
        int n = 0;

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.println("Number < " + (App.round((a + b) / 2, 2)) + "?");
            String x = reader.readLine();
            // round needs to find the number we are looking for
            if (x.equals("yes")) {
                a = (a + b) / 2;
                n += 1;
                if (Math.round(a) == (Math.round(b))) {
                    System.out.println("Your number is " + App.round(a, 2));
                    break;
                }
            }

            else if (x.equals("no")) {
                b = (a + b) / 2;
                n += 1;
                if (Math.round(a) == (Math.round(b))) {
                    System.out.println("Your number is " + App.round(a, 2));
                    break;
                }
            }

            else if (x.equals("exit")) {
                break;
            }

            else {
                System.out.println("You have a mistake in keyboard input. To exit enter \'exit\'");
            }
        }
        return "Completed in " + n + " moves!";
    }

    public static double round(double value, int places) {
        if (places < 0)
            throw new IllegalArgumentException();

        long factor = (long) Math.pow(10, places);
        value = value * factor;
        long tmp = Math.round(value);
        return (double) tmp / factor;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("Hello World!");

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int[] a = new int[5];
        for (int i = 0; i < a.length; i++) {
            a[i] = Integer.parseInt(reader.readLine());
        }

        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }

        ArrayList<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < 100; i++) {
            System.out.println(i);
            list.add(i);
        }

        System.out.println(App.guessNumber());
    }
}