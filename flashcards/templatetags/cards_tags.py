from django import template

from flashcards.models import BOXES, Card

register = template.Library()


@register.inclusion_tag("flashcards/box_list.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        boxes.append({
            "number": box_num,
        })

    return {"boxes": boxes}
    