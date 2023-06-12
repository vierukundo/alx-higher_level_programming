#include "lists.h"
/**
 * iteration_from_tail_to_head - a function that iterates a linked
 * list from tail to head
 * @head: an address of a linked list
 * @index: index of a node from tail
 * Return: returns a node at index
 */
listint_t *iteration_from_tail_to_head(listint_t **head, int index)
{
	listint_t *p = *head;

	int i;

	if (*head == NULL)
		return (NULL);
	for (i = 0; p != NULL; i++)
	{
		if (i == index)
			return (p);
		p = p->next;
	}
	return (NULL);
}
/**
 * is_palindrome - a function in C that checks if
 * a singly linked list is a palindrome.
 * @head: address of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head, *h = *head;

	int i, index = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tail)
	{
		index++;
		tail = tail->next;
	}

	for (i = 0; i < index / 2; i++)
	{
		tail = iteration_from_tail_to_head(head, index - i - 1);
		if (tail == NULL || h == NULL)
			return (0);
		if (h->n != tail->n)
			return (0);
		h = h->next;
	}
	return (1);
}
