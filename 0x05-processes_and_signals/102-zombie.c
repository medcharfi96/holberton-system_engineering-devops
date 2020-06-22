#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - loop without end
 *
 *
 * Return: int(mean true)
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
 * main - main function
 *
 *
 * Return: int (mean true)
 */
int main(void)
{
	int count = 0;

	for (count; count < 5; count++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}
