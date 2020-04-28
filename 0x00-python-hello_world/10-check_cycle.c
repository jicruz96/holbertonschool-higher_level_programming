#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: linked list to check
 * Return: 1 if loop found | 0 if no loop found
 **/
int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = list;

	while (p1->next)
		for (p2 = p1->next, p1 = list; p1 != p2  || p2 == list; p1 = p1->next)
			if (p1->next == p2->next)
				return (1);
	return (0);
}
