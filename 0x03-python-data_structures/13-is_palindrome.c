#include "lists.h"
#include <stdlib.h>

/**
 * get_length_n_data - gets list length an address of its elements
 * @head: pointer to first list node
 * @length: list length
 * Return: array of list adress
 */
int *get_length_n_data(listint_t *head, int *length)
{
	int *data = NULL;
	int count = 0;
	listint_t *temp = head;

	while (head != NULL)
	{
		count++;
		head = head->next;
	}
	*length = count;
	data  = malloc(sizeof(int) * count);
	count = 0;
	while (temp != NULL)
	{
		data[count] = temp->n;
		temp = temp->next;
	}
	return (data);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to first ist node
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int *data = NULL, length = 0, i;
	listint_t *temp = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	data = get_length_n_data(temp, &length);
	for (i = 0; i < length / 2; i++)
	{
		if (temp->n != data[length - i - 1])
		{
			free(data);
			return (0);
		}
		temp = temp->next;
	}
	free(data);
	return (1);
}
