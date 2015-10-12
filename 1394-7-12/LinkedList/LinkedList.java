package javaapplication3;

public class LinkedList {

    Node head;
    int size;

    public LinkedList() {
        size = 0;
        head = null;
    }

    public void push_front(int id, String name) {
        Node new_node = new Node(id, name, head);
        head = new_node;
        size++;
    }

    public void push_back(int id, String name) {
        Node node = new Node(id, name, null);

        if (size == 0) {
            head = node;
        } else {
            Node tmp = head;
            while (tmp.next != null) {
                tmp = tmp.next;
            }
            tmp.next = node;
        }

        size++;
    }

    public void pop_front() {
        head = head.next;
        size--;
    }

    public void pop_back() throws Exception {
        if (head == null) {
            throw new Exception("Empty List");
        } else if (head.next == null) {
            head = null;
            size = 0;
        } else {
            Node tmp = head;
            while (tmp.next.next != null) {
                tmp = tmp.next;
            }
            tmp.next = null;

            size--;
        }
    }

    public void insert(int id, String name, int i) {
        if (i == 0) {
            push_front(id, name);
            return;

        }
        Node tmp = head;

        for (int j = 0; j < i - 1; j++) {
            tmp = tmp.next;
        }
        Node inserted = new Node(id, name, tmp.next);
        tmp.next = inserted;
        size++;
    }

    public void remove(int i) {

        if (i == 0) {

            pop_front();
            return;
        }
        Node tmp = head;

        for (int j = 0; j < i - 1; j++) {
            tmp = tmp.next;
        }
        tmp.next = tmp.next.next;
        size--;
    }

    @Override
    public String toString() {
        String val = "{ ";
        if (size > 0) {
            for (Node n = head; n != null; n = n.next) {
                val += n + " ,";
            }
        }
        return val.substring(0, val.length() - 1) + "}";
    }

}
