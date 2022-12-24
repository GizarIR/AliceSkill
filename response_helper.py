# узнаем имя функции для аналитики
def whoami():
    return sys._getframe(1).f_code.co_name


# В данном модуле располагаются вспомогательные функции
def button(title, payload=None, url=None, hide=False):
    button = {
        'title': title,
        'hide': hide,
    }
    if payload is not None:
        button['payload'] = payload
    if url is not None:
        button['url'] = url
    return button


def image_gallery(image_ids):
    items = [{'image_id': image_id} for image_id in image_ids]
    return {
        'type': 'ImageGallery',
        'items': items,
    }
