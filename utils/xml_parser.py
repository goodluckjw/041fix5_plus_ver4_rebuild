
import xml.etree.ElementTree as ET

def parse_law_xml(file_path, keyword):
    results = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for article in root.iter("조문단위"):
            law_text = ET.tostring(article, encoding='unicode', method='text')
            if keyword in law_text:
                results.append(f"<div style='padding: 10px; background-color: #f9f9f9; border-left: 5px solid #4CAF50;'>{law_text}</div>")
    except Exception as e:
        results.append(f"<div style='color:red;'>⚠️ {str(e)}</div>")
    return results
