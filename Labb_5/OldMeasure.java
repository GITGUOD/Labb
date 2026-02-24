package Labb_5;
import java.util.*;
import java.io.File;                  // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors

public class OldMeasure {

  public static void main(String[] args){
    File file = new File("C:\\Users\\tonny\\OneDrive\\Documents\\EDAA35\\EDAA35-Labb\\Labb_5\\data1.txt");
    ArrayList<Integer> lines = readFile(file);
    int N = 40;
    
    LinkedList<Integer> data = new LinkedList<Integer>();
    Random random = new Random();
    for (int i = 0; i < N; i++) {
        int index = random.nextInt(lines.size());
        data.add(lines.get(index));
    }

    for(int j = 0; j < data.size(); j++) {
        System.out.println("Data: " + data.get(j));
    }
    ListSorter.sort(data);
  }

  public static ArrayList<Integer> readFile(File file) {
    ArrayList<Integer> lines = new ArrayList<>();

    try (Scanner scan = new Scanner(file)) {
        while(scan.hasNextLine()) {
            String line = scan.nextLine();
            lines.add(Integer.parseInt(line));
        }
    } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    }

    return lines;
  }

}
