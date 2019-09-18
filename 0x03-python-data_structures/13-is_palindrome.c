#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - function to reverse lists
 * @head: Pointer to a pointer pointing to a struct
 * Return: Returns a pointer to the first node of the reversed list
**/
void reverse_listint(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *prev = NULL, *next = NULL;

	while (tmp != NULL)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointed linked list
 * Return: 1 if palindrome, -1 if not
**/
int is_palindrome(listint_t **head)
{
	listint_t *right = *head, *rev = *head, *med, *tmp;

	if (*head == NULL)
		return (1);
	if (right->next == NULL)
		return (1);
	while (right != NULL && right->next != NULL)
	{
		right = right->next->next;
		rev = rev->next;
	}
	med = rev;
	reverse_listint(&med);
	tmp = *head;
	while (med != NULL)
	{
		if (med->n == tmp->n)
		{
			med = med->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	return (1);
}
