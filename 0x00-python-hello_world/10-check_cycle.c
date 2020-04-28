#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for a loop in a linked list
 * @list: linked list to check
 * Return: 1 if loop found | 0 if no loop found
 **/

int check_cycle(listint_t *list)
{
	listint_t *p1;

	for (; list; list = list->next)
		for (p1 = list->next; p1; p1 = p1->next)
			if (list == p1)
				return (1);
	return (0);
}
