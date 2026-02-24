package Labb_5;
// Import the Scanner class to read text files
import java.util.*;
import java.io.File;                  // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors

public class Measure {

  public static void main(String[] args){
    File file = new File("C:\\Users\\tonny\\OneDrive\\Documents\\EDAA35\\EDAA35-Labb\\Labb_5\\data1.txt");
    ArrayList<Integer> lines = new ArrayList<>();
    lines = readFile(file);
    
    LinkedList<Integer> data = new LinkedList<Integer>();
    Random random = new Random();
    for (int i = 0; i < 40; i++) {
        int index = random.nextInt(lines.size());
        data.add(lines.get(index));
        System.out.println("Slumpat tal från filen: " + data.add(lines.get(index)));
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
