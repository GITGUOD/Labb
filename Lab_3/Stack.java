import java.util.*;
public interface Stack<E> {
  /**
  * Pushes an element onto this stack.
  * @param e the element to push
  * If the stack is full nothing happens
  */
  void push(E e);

  /**
  * Removes and returns the element 
  * on the top of this stack.
  * @return the element at the top of this stack 
  * or null if this stack is empty
  */
  E pop();

  /**
  * Retrieves, but does not remove, the 
  * element on the top of this stack.
  * @return the element at the top of this stack 
  * or null if this stack is empty
  */
  E peek();

  /**
  * Returns true if this stack contains no elements.
  * @return true if this stack contains no elements
  */
  boolean isEmpty();

  /**
  * Returns true if the stack is full (number elements == max number elements) 
  * @return true if the stack is full
  */
  boolean isFull();

  /**
  * Returns the number of elements in the stack.
  * @return number of elements
  */
  int nrElements();

  /**
  * Removes the top n values of the stack and returns 
  * them in a list. If n is larger than the stack then 
  * pop all elements.
  * @param n number of items to pop
  * @return list a list of values
  */
  List<E> multiPop(int n);

}