package Labb_5;
import java.util.*;

public class ListSorter {

    public static void sort(LinkedList<Integer> data) {
        for (int i = 0; i < data.size(); i++) {
            for (int j = 0; j < data.size() - 1; j++) {
                if (data.get(j) > data.get(j + 1)) {
                    int temp = data.get(j);
                    data.set(j, data.get(j + 1));
                    data.set(j + 1, temp);
                }
            }
        }
    }
}
