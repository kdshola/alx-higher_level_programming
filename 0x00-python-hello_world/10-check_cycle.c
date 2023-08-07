#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: pointer to first node of list
 * Return: 0 if false else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);
	slow = list;
	fast = list->next;
	while (slow && fast->next->next && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
