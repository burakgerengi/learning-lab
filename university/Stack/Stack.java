public class Stack
{
    Object elements[];
    int top;

    public Stack (int n)
    {
        elements = new Object[n];
        top = -1;
    }

    boolean
    isEmpty ()
    {
        return top == -1;
    }

    boolean
    isFull ()
    {
        return top == elements.length - 1;
    }

    void
    push (Object data)
    {
        if (isFull ())
            {
                return;
            }

        top++;
        elements[top] = data;
    }

    Object
    peek ()
    {

        if (isEmpty ())
            {
                return false;
            }

        return elements[top];
    }

    Object
    pop ()
    {

        if (isEmpty ())
            {
                return false;
            }

        Object tmp = peek ();

        top--;
        return tmp;
    }
}
