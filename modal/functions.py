import json

def convert_string_into_data_type(sections):

    sections_list = []

    for section in sections:
        section_data = []
        for data in section.modal_data.all():
            data_json = json.loads(data.data)

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