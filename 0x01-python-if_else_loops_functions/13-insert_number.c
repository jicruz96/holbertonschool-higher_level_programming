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
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *ptr = *head;
	listint_t *prev = *head;

	if (new_node != NULL)
	{
		while (ptr != NULL || prev != NULL)
		{
			if (ptr == NULL || ptr->n >= number)
			{
				new_node->n = number;
				if (ptr == *head)
					*head = new_node;
				else
					prev->next = new_node;
				new_node->next = ptr;
				return (new_node);
			}
			prev = ptr;
			ptr = ptr->next;
		}
		free(new_node);
	}
	return (NULL);
}
