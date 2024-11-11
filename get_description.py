import os


def get_description_from_file(item_name):
    file_path = os.path.join('description_whiskey.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()


            marker = f"[{item_name}]"
            start_index = content.find(marker)

            if start_index != -1:

                start_index += len(marker) + 1
                end_index = content.find("[", start_index)
                if end_index == -1:
                    description = content[start_index:].strip()
                else:
                    description = content[start_index:end_index].strip()
                return description
            else:
                return "Описание не найдено"
    else:
        return "Файл не найден"
