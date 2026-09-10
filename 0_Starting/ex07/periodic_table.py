def parse_element_line(line):
    if not line.strip():
        return None
    
    name_part, attributes_part = line.split("=", 1)
    name = name_part.strip()
    
    attr_dict = {}
    attributes = attributes_part.split(",")
    for attr in attributes:
        if ":" in attr:
            key, value = attr.split(":", 1)
            attr_dict[key.strip()] = value.strip()
            
    return {
        "name": name,
        "position": int(attr_dict.get("position", 0)),
        "number": attr_dict.get("number", ""),
        "small": attr_dict.get("small", ""),
        "molar": attr_dict.get("molar", ""),
        "electron": attr_dict.get("electron", "")
    }

def generate_html(elements):
    html_content = [
        "<!DOCTYPE html>",
        "<html lang=\"en\">",
        "<head>",
        "    <meta charset=\"UTF-8\">",
        "    <title>Periodic Table</title>",
        "    <style>",
        "        body { font-family: Arial, sans-serif; background-color: #f4f4f9; }",
        "        table { border-collapse: collapse; margin: 20px auto; }",
        "        td { border: 1px solid #333; padding: 5px; text-align: center; vertical-align: middle; width: 85px; height: 100px; box-sizing: border-box; background-color: white; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); }",
        "        .empty { border: none; background-color: transparent; box-shadow: none; }",
        "        h4 { margin: 0; font-size: 0.8em; text-align: left; color: #555; }",
        "        h1 { margin: 5px 0; font-size: 1.8em; font-weight: bold; color: #222; }",
        "        ul { list-style-type: none; padding: 0; margin: 0; }",
        "        li { margin-bottom: 2px; }",
        "        .molar { font-size: 0.75em; color: #555; }",
        "        .name { font-size: 0.65em; font-weight: bold; color: #777; text-transform: uppercase; }",
        "    </style>",
        "</head>",
        "<body>",
        "    <table>",
        "        <tr>"
    ]

    current_col = 0
    for element in elements:
        position = element["position"]
        
        if position < current_col:
            while current_col <= 17:
                html_content.append("            <td class=\"empty\"></td>")
                current_col += 1

            html_content.append("        </tr>")
            html_content.append("        <tr>")
            current_col = 0
            
        while current_col < position:
            html_content.append("            <td class=\"empty\"></td>")
            current_col += 1
            
        cell = (
            f"            <td>\n"
            f"                <h4>{element['number']}</h4>\n"
            f"                <h1>{element['small']}</h1>\n"
            f"                <ul>\n"
            f"                    <li class=\"name\">{element['name']}</li>\n"
            f"                    <li class=\"molar\">{element['molar']}</li>\n"
            f"                </ul>\n"
            f"            </td>"
        )
        html_content.append(cell)
        current_col += 1

    while current_col <= 17:
        html_content.append("            <td class=\"empty\"></td>")
        current_col += 1

    html_content.extend([
        "        </tr>",
        "    </table>",
        "</body>",
        "</html>"
    ])
    
    return "\n".join(html_content)

def main():
    elements = []
    
    try:
        with open("periodic_table.txt", "r") as f:
            for line in f:
                parsed_element = parse_element_line(line)
                if parsed_element:
                    elements.append(parsed_element)
    except FileNotFoundError:
        print("Error: periodic_table.txt not found.")
        return

    html_output = generate_html(elements)
    
    with open("periodic_table.html", "w") as f:
        f.write(html_output)

if __name__ == "__main__":
    main()