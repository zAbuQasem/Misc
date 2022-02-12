#include<stdlib.h>
#include<stdio.h>

/**
 * This code needs to be fixed..
 * Number of arrays need to figured better
 * Nozeros functions need work..
 */

int * sum(const int *arr, int n);
int * nozeros(const int *arr);
void print(const int *arr);

int main(int *argc, char **argv){
	printf("[~~] Learning is Pain.. [~~]\n\n");
	
	int array[] = {1,2,3};
	int array2[] = {1,0,2,0,3,4,0};
	int * res  = sum(array, 3);
	int * res2 = nozeros(array2);
	printf("[+] Double the numbers of an array: ");
	print(res);
	printf("\n\n[+] No zeros in an array: ");
	print(res2);
	return 0;
}


int * sum(const int *arr, int n){
        if(arr == NULL){
                exit(1);
        }

	int * result = (int *) malloc(n * sizeof(int));

        for(int i=0; i < 3 ; i++){
		result[i] = (arr[i] * 2);
        }

        return result;
}

int * nozeros(const int *arr){
	size_t n = sizeof(arr) / sizeof(int);
	int * result = (int *) malloc(n * sizeof(int));
	for(int i=0; i<n; i++){
		if(arr[i] != 0){
			result[i] += arr[i];
		}
	}
	return result;
}

void print(const int *arr){
	printf("[");
	size_t n = sizeof(arr) / sizeof(int);
	for(int i=0; i<n-1; i++){
                printf("%d, ",arr[i]);
        }
	printf("%d]", arr[n-1]);
}


