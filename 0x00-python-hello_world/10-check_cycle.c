#include "lists.h"
/**
 * check_cycle - function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prev =list;
	listint_t *current = list;

	if (!list)
		return (0);
	while (prev && current && current->next)
	{
		prev = prev->next;
		current = current->next->next;
		if (prev == current)
			return (1);
	}
	return (0);
}
