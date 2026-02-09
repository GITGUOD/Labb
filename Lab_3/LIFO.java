import java.util.LinkedList;
import java.util.List;

public class LIFO<E> implements Stack<E>{

     /**
     * Pushes an element onto this stack.
     * @param e the element to push
     * If the stack is full nothing happens
     */
    private LinkedList<E> stack;
    private int maxSize;

    public LIFO(int maxSize) {
        this.maxSize = maxSize;
        stack = new LinkedList<E>();

    }

    public void push(E e) {
        if(!isFull()) {
            stack.push(e);
        }

    }

    /**
     * Removes and returns the element 
     * on the top of this stack.
     * @return the element at the top of this stack 
     * or null if this stack is empty
     */
    public E pop() {
        if(!isEmpty()) {
            return stack.pop();
        }
        return null;

    }

    /**
     * Retrieves, but does not remove, the 
     * element on the top of this stack.
     * @return the element at the top of this stack 
     * or null if this stack is empty
     */

    public E peek() {
        if(!isEmpty()) {
            return stack.peek();
        }
        return null;

    }

    /**
     * Returns true if this stack contains no elements.
     * @return true if this stack contains no elements
     */
    public boolean isEmpty() {
        return stack.isEmpty();

    }

    /**
     * Returns true if the stack is full (number elements == max number elements) 
     * @return true if the stack is full
     */
    public boolean isFull() {
        return stack.size() == maxSize;

    }

    /**
     * Returns the number of elements in the stack.
     * @return number of elements
     */
    public int nrElements() {
        return stack.size();

    }

    /**
     * Removes the top n values of the stack and returns 
     * them in a list. If n is larger than the stack then 
     * pop all elements.
     * @param n number of items to pop
     * @return list a list of values
     */
    public List<E> multiPop(int n) {
        List<E> poppedElements = new LinkedList<E>();
        for(int i = 0; i < n; i++) {
            if(!isEmpty()) {
                poppedElements.add(pop());
            }
        }
        return poppedElements;

    }
}
