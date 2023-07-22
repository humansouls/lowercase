def make_lowercase_strings(strings_file):
    with open(strings_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(strings_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if '=' in line:
                key, value = line.split('=')
                value = value.strip()
                if value.startswith('"') and value.endswith('";'):
                    value = value[1:-2] 
                    value = value.lower()
                    line = f'{key} = "{value}";\n'
            file.write(line)

make_lowercase_strings('example.strings')
