import json

def convert_string_into_data_type(sections):

    sections_list = []

    for section in sections:
        section_data = []
        for data in section.modal_data.all():
            try: 
                data_json = json.loads(data.data)
            except:
                data_json = data.data

            data_dict = {
                'data': data_json,
                'data_style': data.data_style,
                'title': data.title,
                'image': data.image,
                'id': data.id,
            }
            section_data.append(data_dict)

        section_dict = {
            'title': section.title,
            'information': section.information,
            'data': section_data,
            'collapse': section.collapse,
            'id': section.id,
            
        }
        sections_list.append(section_dict)

    return sections_list

def format_data_for_database(request):
    
    data_style = request.POST.get('data_style')

    # list
    if data_style == 'List': 
        data = []
        item_count = 1
        while True:
            input_name = f'item-{item_count}'
            data_item = request.POST.get(input_name)
            if not data_item:
                break
            data.append(data_item)
            item_count += 1
        
    # Defnintion
    elif data_style == 'Definition':
        data = request.POST.get('definition')
    # 3d print
    elif data_style == 'Image':
        attriubteArray = []
        item_count = 1
        while True:
            input_name_attriubte = f'attribute-{item_count}'
            input_name_value = f'value-{item_count}'
            attriubte_item = request.POST.get(input_name_attriubte)
            value_item = request.POST.get(input_name_value)
            if not attriubte_item:
                break
            data_dict = {
                'title': attriubte_item,
                'value': value_item
            }
            attriubteArray.append(data_dict)
            item_count += 1

        data = {
            "description": request.POST.get('description'),
            "attributes": attriubteArray,
        }
    elif data_style == 'Code':
        data = request.POST.get('code')

    data = str(data).replace("'", '"')

    return str(data)