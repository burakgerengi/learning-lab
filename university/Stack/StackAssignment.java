import java.util.Scanner;

public class StackAssignment
{

    private static final char[] openingBrackets = { '(', '[', '{' };
    private static final char[] closingBrackets = { ')', ']', '}' };

    public static void
    main (String[] args)
    {
        String expression = getUserInput ();

        if (isBalanced (expression))
            {
                System.out.println ("Valid brackets.");
            }
        else
            {
                System.out.println ("Invalid brackets.");
            }
    }

    private static String
    getUserInput ()
    {
        Scanner scanner = new Scanner (System.in);

        System.out.print ("Brackets Checker\nEnter expression: ");
        String expression = scanner.nextLine ();
        scanner.close ();

        return expression;
    }

    private static boolean
    isBalanced (String expression)
    {

        Stack stack = new Stack (expression.length ());

        for (int i = 0; i < expression.length (); i++)
            {

                char ch = expression.charAt (i);

                if ("([{".indexOf (ch) != -1)
                    {
                        stack.push (ch);
                    }

                else if (")]}".indexOf (ch) != -1)
                    {

                        if (stack.isEmpty ())
                            {
                                return false;
                            }

                        char top = (char)stack.peek ();

                        if (matches (top, ch))
                            {
                                stack.pop ();
                            }

                        else
                            {
                                return false;
                            }
                    }
            }

        return stack.isEmpty ();
    }

    private static boolean
    matches (char opening, char closing)
    {

        for (int i = 0; i < openingBrackets.length; i++)
            {

                if (opening == openingBrackets[i] && closing == closingBrackets[i])
                    {
                        return true;
                    }
            }

        return false;
    }
}
