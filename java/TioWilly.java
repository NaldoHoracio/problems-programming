import java.util.*;

public class TioWilly
{
    public static void main(String[] args)
    {
        int MAXSIZE = 2;
        boolean aux = true;
        int n, equal = 0, cont = 0;
        int[] array = new int[MAXSIZE];

        Scanner input = new Scanner(System.in);

        for(; aux; cont++)
        {
            for(int i = 0; i < MAXSIZE; ++i) array[i] = input.nextInt();

            if(array[0] == -1 && cont > 0)
            {
                aux = false;
                break;
            }
            
            n = input.nextInt();

            for(int j = 0; j < MAXSIZE; ++j) if(array[j] == n) equal++;

            System.out.printf("%d appeared %d times\n", n, equal);
            equal = 0;
        }
    }
}