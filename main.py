from box import BaseBox, Box
from handlers import headers_is_right, send_requests_to_buy


headers_is_right()

box_info = BaseBox()
avalible_boxes = box_info.get_avalible_boxes()
box_info.log_info_boxes(avalible_boxes)

selected_box = str(input('\nNumber of box: '))
amount_boxes = int(input(f'\nAmount boxes (Max: {avalible_boxes[selected_box]["limit_amount"]}): '))

product_id = avalible_boxes[selected_box]['product_id']
box = Box(product_id=product_id, amount=amount_boxes)
start_sale_time = box._get_start_sale_time

print('Waiting for start')
send_requests_to_buy(box, start_sale_time)
