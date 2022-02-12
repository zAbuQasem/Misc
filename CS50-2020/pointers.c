#include<stdlib.h>
#include<stdio.h>

int main(int *argc, char **argv){
	printf("[~~] Learning is Pain..[~~]\n\n");
	char *arr[] = {"one", "two", "three", "four"};
	printf("[+] arr[0]: [%s] and located at: [%p]\n", arr[0], arr[0]);
	printf("[+] arr[1]: [%s] and located at: [%p]\n", arr[1], arr[1]);
	printf("[+] arr[2]: [%s] and located at: [%p]\n", arr[2], arr[2]);
	printf("[+] arr[3]: [%s] and located at: [%p]\n\n", arr[3], arr[3]);

	int var = 10;

	int *x = &var;
	printf("\n[+] x points to: [%p] and contains: [%d]", &x, *x);

	printf("\n[-] Changing the value of var");
	*x = 50;
	printf("\n[+] x points to: [%p] and contains: [%d]", &x, *x);
	return 0;
}
