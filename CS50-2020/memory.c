#include<stdlib.h>
#include<stdio.h>

int main(int *argc, char **argv){
	printf("[-] Learning is Pain..\n");

	int buffer[50];
	int buffer2 [25];

	int *arr1 = (int *) malloc(sizeof(buffer));
	int *arr2 = (int *) malloc(sizeof(buffer2));

	if(arr1 == NULL){
		printf("[!] Error allocating memory for arr1");
	}else if(arr2 == NULL){
		printf("[!] Error allocating memory for arr2");
	}

	printf("[+] arr1 is located at: [%p] and contains: [%d]\n", arr1, *arr1);
	printf("[+] arr2 is located at: [%p] and contains: [%d]\n", arr2, *arr2);

	free(arr1);
	free(arr2);

	printf("[+] arr1 after freeing the heap: [%p] and contains: [%d]\n", arr1, *arr1);
        printf("[+] arr2 after freeing the heap: [%p] and conatins: [%d]\n", arr2, *arr2);

	arr1 = NULL;
	arr2 = NULL;

	return 0;

}

