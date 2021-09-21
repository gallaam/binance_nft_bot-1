from box import BaseBox, Box
from handlers import send_requests_to_buy


box_info = BaseBox()
avalible_boxes = box_info.get_avalible_boxes()
box_info.log_info_boxes(avalible_boxes)


selected_box = str(input('\nНомер коробки: '))
amount_boxes = int(input('\nКоличество коробок (1-20): '))

product_id = avalible_boxes[selected_box]['product_id']
box = Box(product_id=product_id, amount=amount_boxes)
start_sale_time = box._get_start_sale_time


print('Waiting for start')
send_requests_to_buy(box, start_sale_time)
