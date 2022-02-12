#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char **argv){
	char * string = "Hello world!"; // Dynamically allocated at the heap but as read only!
	char * name = (char * ) malloc(sizeof(char)* 100);
	name = "zeyad";
	free(name);
	printf("My name is: [%s] pointing at: [%p]", name, name);
	name = "khaled";
	printf("\nMy name is: [%s] pointing at: [%p]", name, name);
	return 0;

}
