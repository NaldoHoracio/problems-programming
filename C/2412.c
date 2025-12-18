#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//#include <unistd.h>

int main()
{
    int N, E, parcela1, parcela2, soma, i, j, *arr, extravagancia = false;
    //printf("Digite N e E:\n");
    scanf("%d %d", &N, &E);

    arr = (int*)malloc(N * sizeof(int));

    //printf("Digite os inteiros G\n");
    for(i = 0; i < N; ++i)
    {
        scanf("%d", &arr[i]);
    }
    
    for(i = 0; i < N; ++i)
    {
        parcela1 = arr[i];

        for(j = i+1; j < N; j++)
        {
            parcela2 = arr[j];

            soma = parcela1 + parcela2;

            //printf("SOMA: %d\n", soma);

            if(soma == E)
            {
                extravagancia = true;
                break;
            }
        }
        if(extravagancia == true){break;}      
    }

    (extravagancia == true) ? printf("SIM\n") : printf("NAO\n");
    free(arr);

    return 0;
}