#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number to insert into list
 * Return: address of new node | NULL if insertion failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *ptr, *prev;

	if (node && head)
	{
		ptr = *head;
		prev = *head;
		while (ptr || prev)
		{
			if (ptr == NULL || ptr->n >= number)
			{
				node->n = number;
				if (ptr == *head)
					*head = node;
				else
					prev->next = node;
				node->next = ptr;
				return (node);
			}
			prev = ptr;
			ptr = ptr->next;
		}
		free(node);
	}
	return (NULL);
}
