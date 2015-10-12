package javaapplication3;

public class Node {

    int number;
    String name;
    Node next;

    public Node(int number, String str, Node node) {
        this.name = str;
        this.next = node;
        this.number = number;
    }

    @Override
    public String toString() {
        return "[" + this.name + " , " + this.number + "]";
    }

}
