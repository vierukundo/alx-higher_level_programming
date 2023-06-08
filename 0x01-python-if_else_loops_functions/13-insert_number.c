#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function that insets number in sorted list
 * @head: pointer to list
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head, *new, *next_node;

	while (h)
	{
		next_node = h->next->next;
		if (next_node->n >= number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = next_node;
			h->next = new;
			return (new);
		}
		h = h->next;
	}
	return (NULL);
}
