#include <fcntl.h>
#include <unistd.h>
#include <stddef.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - function to create 5 zombies
 *
 * Return: 0 if succesfull
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry point
 *
 * Return: 0 if succesful 1 otherwise
 */
int main(void)
{
	int pid, i;

	for (i = 0 ; i < 5 ; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}

		else if (pid < 0)
		{
			perror("fork failed");
			return (1);
		}
	}

	infinite_while();
	return (0);
}
