import argparse
import os
import re

def slugify(text):
    """Simple slugify: translate German umlauts and lowercase, replace non-alphanumerics with hyphens."""
    text = text.lower()
    # basic translation for German characters
    replacements = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'}
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    # replace non-alphanumeric with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def split_markdown(input_path, output_dir):
    # Read the entire file
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract title and date
    title = ''
    date_line = ''
    for line in lines:
        if line.startswith('# '):
            title = line.strip()
        elif line.lower().startswith('datum:'):
            date_line = line.strip()
        if title and date_line:
            break

    if not title:
        raise ValueError("Konnte den Haupttitel (Zeile mit '# ') nicht finden.")
    if not date_line:
        raise ValueError("Konnte die Datumszeile (beginnt mit 'Datum:') nicht finden.")

    # Prepare output directory
    os.makedirs(output_dir, exist_ok=True)

    # Find sections
    sections = []  # list of (section_title, content_lines)
    current_section = None

    for line in lines:
        match = re.match(r'##\s+(.+)', line)
        if match:
            if current_section:
                sections.append(current_section)
            sec_title = match.group(1).strip()
            current_section = (sec_title, [line])
        else:
            if current_section:
                current_section[1].append(line)
    if current_section:
        sections.append(current_section)

    # Base slug for filename
    base_slug = slugify(title.lstrip('# '))

    # Write each section with numbering
    chapter_counter = 1
    for sec_title, content_lines in sections:
        # Assign number: 'Präambel' gets 00, others sequential
        if sec_title.lower() == 'präambel':
            num = 0
        else:
            num = chapter_counter
            chapter_counter += 1
        num_str = f"{num:02d}"

        sec_slug = slugify(sec_title)
        filename = f"{num_str}-{base_slug}-{sec_slug}.md"
        out_path = os.path.join(output_dir, filename)
        with open(out_path, 'w', encoding='utf-8') as out_file:
            out_file.write(f"{title}\n")
            out_file.write(f"{date_line}\n\n")
            out_file.writelines(content_lines)
        print(f"Erstellt: {out_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Teile ein Markdown-Dokument an den H2-Überschriften in einzelne Dateien und nummeriere sie.'
    )
    parser.add_argument('input_file', help='Pfad zur Eingabe-Markdown-Datei')
    parser.add_argument('output_dir', help='Verzeichnis für die Ausgabe-Dateien')
    args = parser.parse_args()
    split_markdown(args.input_file, args.output_dir)
