#include "lists.h"
/**
 * check_cycle - function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	int flag = 1, i;

	listint_t *head = list, *h;

	do {
		list = list->next;
		h = head;
		for (i = 0; i < flag; i++)
		{
			if (list == h)
				return (1);
			h = h->next;
		}
		list = list->next;
		flag++;
	} while (list);
	return (0);
}
