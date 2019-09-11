#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Func that inserts a sorted number in a linked list
 * @head: Pointer to the pointer of the head
 * @number: Number stored by the node
 * Return: Returns the new list with the added node
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *tmp;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	tmp = *head;

	while (tmp->next != NULL && tmp->next->n < number)
		tmp = tmp->next;
	newNode->next = tmp->next;
	tmp->next = newNode;
return (tmp);
}
