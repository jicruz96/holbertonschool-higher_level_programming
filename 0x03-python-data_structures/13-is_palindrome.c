#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list
 * Return: 1 if palindrome | 0 if not
 **/
int is_palindrome(listint_t **head)
{
	listint_t *tail = NULL, *tmp = *head, *prev;
	int result = 1;

	while (result && tmp && tmp != tail)
	{
		for (prev = tmp; prev->next != tail;)
			prev = prev->next;

		tail = prev;

		if (tmp->n != tail->n)
			result = 0;

		if (tmp == tail || tmp->next == tail)
			tmp = NULL;
		else
			tmp = tmp->next;
	}
	free_listint(tmp);
	return (result);
}
