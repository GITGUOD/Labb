package Labb_5;

import java.util.*;
import java.io.*;

public class Measure {

    public static void main(String[] args) {

        if (args.length < 3) {
            System.out.println("Usage: java Measure <inputfile> <outputfile> <N>");
            return;
        }

        String inputFile = args[0];
        String outputFile = args[1];
        int N = Integer.parseInt(args[2]);

        LinkedList<Integer> data = readFile(inputFile);

        try (PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {

            writer.println("Iteration,Time(ns)");
            long totalTime = 0;

            LinkedList<Integer> copy = new LinkedList<>(data);
            for (int i = 0; i < N; i++) {

                long start = System.nanoTime();
                //Collections.sort(copy);
                ListSorter.sort(copy);
                long end = System.nanoTime();

                long time = end - start;
                totalTime += time;

                writer.println(i + "," + time);
            }

            System.out.println("Average time: " + (totalTime / N));

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static LinkedList<Integer> readFile(String filename) {
        LinkedList<Integer> list = new LinkedList<>();

        try (Scanner scan = new Scanner(new File(filename))) {
            while (scan.hasNextLine()) {
                list.add(Integer.parseInt(scan.nextLine().trim()));
            }
        } catch (FileNotFoundException e) {
            System.out.println("Could not find file: " + filename);
        }

        return list;
    }
}
