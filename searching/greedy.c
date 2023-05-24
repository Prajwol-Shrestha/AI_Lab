#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, j, min_index, temp;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d integers:\n", n);
    for(i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    // Implementing the greedy search algorithm
    for(i = 0; i < n-1; i++)
    {
        min_index = i;
        for(j = i+1; j < n; j++)
        {
            if(arr[j] < arr[min_index])
                min_index = j;
        }
        temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }

    printf("The sorted array is:\n");
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}
