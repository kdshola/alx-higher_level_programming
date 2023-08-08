#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: pointer to first list node
 * @number: data to insert to node
 * Return: address of node or NULL of it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = *head, *ahead = (*head)->next;

	while (current->next)
	{
		if ((current->n <= number) && ((ahead->n >= number) || !ahead))
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = NULL;
			current->next = new;
			new->next = ahead;
			return (new);
		}
		current = current->next;
		ahead = ahead->next;
	}
	return (NULL);
}
