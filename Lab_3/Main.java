public class Main {

    public static void main(String[] args) {

        Stack<String> stack = new LIFO<String>(5);
        stack.push("A"); stack.push("B"); stack.push("C");

        //Stacken ska nu innehålla A, B och C, C överst

        System.out.println(stack.pop()); // returnerar "C"
        stack.push("D");

        System.out.println(stack.peek()); // returnerar "D"
        System.out.println(stack.nrElements()); // returnerar 3

        for(String s : stack.multiPop(stack.nrElements())) {
            System.out.println(s); // skriver ut D, B och A
        }
    }

}
