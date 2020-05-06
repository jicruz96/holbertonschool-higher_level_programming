#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list
 * Return: 1 if palindrome | 0 if not
 **/
int is_palindrome(listint_t **head)
{
	int array[1024];
	int i = 0, j = 0, len = 0;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
		return (1);

	for (tmp = *head; tmp != NULL; tmp = tmp->next)
		array[i++] = tmp->n;

	if (j > (i - 1) / 2)
		printf("NO LOOP FOR YOU\n");
	else
		printf("LOOP TIME!\n");

	for (len = i - 1; j <= len / 2; j++)
	{
		printf("\tarray[%d] = %d\tarray[%d] = %d\n", j, array[j], len - j, array[len - j]);
		if (array[j] != array[len - j])
			return (0);
	}
	return (1);
}
