#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list
 * Return: 1 if palindrome | 0 if not
 **/
int is_palindrome(listint_t **head)
{
	int *array;
	int i = 0, j = 0, len = 0, result = 1;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
		return (1);

	for (tmp = *head; tmp != NULL; tmp = tmp->next)
		array[i++] = tmp->n;

	array = malloc(sizeof(int) * i);

	for (len = i - 1; result && j < len / 2; j++)
		if (array[j] != array[len - j])
			result = 0;

	free(array);
	return (1);
}
