#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 *infinite_while - an infinite while loop
 *Return:0
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
 *main - creates 5 zombie processes
 *
 *Return:0
 */
int main(void)
{
	pid_t pid;
	int n = 0;

	while (n < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			n++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
