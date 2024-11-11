import os


def get_description_from_file(item_name):
    file_path = os.path.join('description_whiskey.txt')  # Путь к файлу с описаниями

    # Проверяем, существует ли файл
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Ищем нужное описание по метке
            marker = f"[{item_name}]"
            start_index = content.find(marker)

            if start_index != -1:
                # Ищем конец описания, можно считать, что оно заканчивается перед следующим маркером
                start_index += len(marker) + 1  # Пропускаем сам маркер и пробел
                end_index = content.find("[", start_index)  # Находим следующий маркер
                if end_index == -1:
                    description = content[start_index:].strip()  # Если нет следующего маркера
                else:
                    description = content[start_index:end_index].strip()
                return description
            else:
                return "Описание не найдено"
    else:
        return "Файл не найден"
