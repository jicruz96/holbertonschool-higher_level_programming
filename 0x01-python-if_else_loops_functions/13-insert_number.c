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
	listint_t *new_node, *ptr, *prev;

	/* Return NULL if head pointer is NULL (i.e. empty list) */
	if (head == NULL || *head == NULL)
		return (NULL);

	/* Allocate memory for new struct */
	new_node = malloc(sizeof(listint_t));

	/* If memory allocation failed, return NULL */
	if (new_node == NULL)
		return (NULL);

	/* Store number into the node */
	new_node->n = number;

	/* Initialize our pointers to point to head node */
	ptr = *head;
	prev = *head;

	/* Traverse through the list */
	while (ptr != NULL)
	{
		if (ptr->n >= number)
		{
			prev->next = new_node;
			new_node->next = ptr;
			return (new_node);
		}
		prev = ptr;
		ptr = ptr->next;
	}
	/**
	 * If we're here, then number is the smallest number
	 * in the list. Set new_node as the new head node
	 **/
	new_node->next = *head;
	*head = new_node;
	return (*head);
}
