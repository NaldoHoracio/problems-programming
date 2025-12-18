import java.io.*;
import java.util.Scanner;

public class MaioresDoSorteio
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int d = input.nextInt();

        int[] array = new int[n];

        System.out.printf("Digite os %d numeros:\n", n);
        for(int i = 0; i < n; ++i)
        {
            array[i] = input.nextInt();
        }

        System.out.printf("Ordenando com quickSort...\n");
        quickSort(array, 0, array.length-1);

        int[] five_largest = new int[5];
        for(int j = 0; j < 5; ++j) five_largest[j] = -1;

    }

    // quickSort
    //This method sorts the input array in descending order using quick sort
    public static void quickSort(int[] array, int low, int high)
    {
 
        int i = low;
        int j = high;
        int temp;
        int middle = array[(low + high)/2];
 
        while (i < j)
        {
            while (array[i] > middle)
            {
                i++;
            }
            while (array[j]<middle)
            {
                j--;
            }
            if (j >= i)
            {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
                i++;
                j--;
            }
        } 
        if (low < j)
        {
            quickSort(array, low, j);
        }
        if (i < high)
        {
            quickSort(array, i, high);
        }
    }
}