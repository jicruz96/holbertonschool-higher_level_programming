#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: linked list to check
 * Return: 1 if loop found | 0 if no loop found
 **/
int check_cycle(listint_t *list)
{
	listint_t *p1;

	if (list)
	{
		for (p1 = list->next; p1; list = list->next, p1 = p1->next)
		{
			if (list->next == p1->next)
				return (1);
			p1 = p1->next;
			if (!p1)
				break;
		}
	}
	return (0);
}
