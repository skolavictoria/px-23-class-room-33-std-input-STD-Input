#include <stdio.h>

int main(int argc, char *argv[]) {
    // Print the program name
    printf("Program Name: %s\n", argv[0]);

    // Print the number of arguments
    printf("Number of Arguments: %d\n", argc - 1); // Excluding program name

    // Print each argument
    for (int i = 1; i < argc; i++) { // Start from 1 to skip the program name
        printf("Argument %d: %s\n", i, argv[i]);
    }

    return 0;
}
