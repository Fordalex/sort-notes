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
            print(type(data_json))

            data_dict = {
                'data': data_json,
                'data_style': data.data_style,
                'title': data.title,
            }
            section_data.append(data_dict)

        section_dict = {

            'title': section.title,
            'information': section.information,
            'data': section_data,
            'id': section.id,
            
        }
        sections_list.append(section_dict)

    return sections_list

def format_data_for_database(request):
    
    data_style = request.POST.get('data_style')

    if data_style == 'List': 
        data_list = []
        item_count = 1
        while True:
            input_name = f'item-{item_count}'
            data_item = request.POST.get(input_name)
            if not data_item:
                break
            data_list.append(data_item)
            item_count += 1
        data = str(data_list).replace("'", '"')
    elif data_style == 'Definition':
        data = request.POST.get('definition')

    return str(data)