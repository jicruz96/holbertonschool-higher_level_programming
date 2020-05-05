#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list
 * Return: 1 if palindrome | 0 if not
 **/
int is_palindrome(listint_t **head)
{
	listint_t *tail = NULL, *tmp = *head;
	int result = 1;

	while (result && tmp && tmp != tail)
	{
		prev_node(&tail, tmp);
		if (tmp->n != tail->n)
			result = 0;
		next_node(&tmp, tail);
	}
	free_listint(tmp);
	return (result);
}
/**
 * next_node - checks if a number is a palindrome
 * @current: current node. to be set to next node.
 * @tail: end of list. not necessarily NULL.
 * Return: void
 **/

void next_node(listint_t **current, listint_t *tail)
{
	if (*current == tail || (*current)->next == tail)
		*current = NULL;
	else
		*current = (*current)->next;
}

/**
 * prev_node - retrieves the previous node of a list
 * @current: current node. to be set to previous node.
 * @head: starting position in linked list
 * Return: void
 **/
void prev_node(listint_t **current, listint_t *head)
{
	listint_t *previous = head;

	while (previous && previous->next != *current)
		previous = previous->next;

	*current = previous;
}
