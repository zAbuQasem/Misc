#include<stdlib.h>
#include<stdio.h>
#include<string.h>

/**
 *This function prints all characters from a file individually sepereated by a newline
 */
void readchar(FILE *file);


/**
 * This function prints line by line from a file
*/
void readline(FILE *file, int buffer, char *line);

/*
 * This function demonstrates how to write to a file
 *
 */
void writefile(FILE *file, const char *message);


int main(int argc, char **argv){
	printf("[!] Learning sucks [!]\n");
	FILE *f = fopen("/etc/passwd", "r");
	if (f == NULL){
		printf("[!] Unable to openfile");
		exit(1);
	}

	//readchar(f);
	

	char line [100]; // To store the lines into
	readline(f, 100, line);
	
	fclose(f);

	FILE *fw = fopen("data.bin", "w");
	char *message = "Some human un-readable data ++"; 
	writefile(fw,message);
	fclose(fw);
	return 0;
}

void readchar(FILE *file){
	printf("[+] Reading a single character from the file..\n");
	char chr = fgetc(file);
	while (chr != EOF){
		printf("[chr] = %c\n", chr);
		chr = fgetc(file); // Pointing to the next character
	}
}

void readline(FILE *file, int buffer, char *line){
	printf("[+] Reading a single character from the file..\n");
	char *lines = fgets(line, buffer , file);
	while (lines!= NULL){
		printf("[line] = %s", line);
                lines = fgets(line, buffer , file); // Pointing to the next line
	}

}

void writefile(FILE *file, const char *message){
	printf("\n[+] Writing to a binary file\n");
	fwrite(message, sizeof(char), strlen(message),  file); // without using strlen it will read until reaches the maximum assigned number of bytes

}
